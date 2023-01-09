import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

from scipy.cluster.hierarchy import dendrogram

def plot_features_scores(X, scores, method='univariate',
    metric_label=r'$-log(p_{value})$', figsize=(10, 20)):
    scores_df = pd.DataFrame({'scores': scores, 'columns': X.columns}) \
        .sort_values('scores', ascending=False)
    plt.figure(figsize=figsize)
    sns.barplot(data=scores_df, x='scores', y='columns', color='blue')
    plt.grid(True)
    plt.title(f'Feature {method} score')
    plt.xlabel(f'{method.capitalize()} score ({metric_label})')
    plt.ylabel('')
    plt.show()


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


def plot_clustering(X_red, labels, title=None):
    x_min, x_max = np.min(X_red, axis=0), np.max(X_red, axis=0)
    X_red = (X_red - x_min) / (x_max - x_min)

    plt.figure(figsize=(6, 4))
    for digit in digits.target_names:
        plt.scatter(
            *X_red[y == digit].T,
            marker=f"${digit}$",
            s=50,
            c=plt.cm.nipy_spectral(labels[y == digit] / 10),
            alpha=0.5,
        )

    plt.xticks([])
    plt.yticks([])
    if title is not None:
        plt.title(title, size=17)
    plt.axis("off")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])


def plot_risk_cost_reduction(df, prob_column, risk_reduction, base_adherance_percentage, post_cost, pre_cost):
    fig, ax = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

    adherence_percentages = np.arange(base_adherance_percentage, 1.0, 0.1)
    print(f'{adherence_percentages=}')

    mean_risk_reductions = [
        np.where(
            df.index.isin(df.sample(frac=adherance_percentage).index),
            df[prob_column] * risk_reduction,
            df[prob_column]
        ).mean()
        for adherance_percentage in adherence_percentages
    ]
    print(f'{mean_risk_reductions=}')

    total_population = df.shape[0]
    cost_reductions = [
        total_population * post_cost - total_population * adherance_percentage * (post_cost - pre_cost)
        for adherance_percentage in adherence_percentages
    ]
    print(f'{cost_reductions=}')

    sns.lineplot(x=adherence_percentages * 100, y=mean_risk_reductions, ax=ax[0], markers=True)
    ax[0].xaxis.set_major_formatter(mtick.PercentFormatter())
    ax[0].set_ylabel('Mean Risk Reduction (probability)')

    sns.lineplot(x=adherence_percentages * 100, y=cost_reductions, ax=ax[1], markers=True)
    ax[1].xaxis.set_major_formatter(mtick.PercentFormatter())
    ax[1].set_ylabel('Cost Reduction (€)')

    fig.text(0.5, 0.04, 'Percentage of adherance', ha='center')
    fig.suptitle('Cost and risk analysis')

