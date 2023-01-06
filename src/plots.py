import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_features_scores(
    X, scores, method='univariate', metric_label=r'$-log(p_{value})$'):
    scores_df = pd.DataFrame({'scores': scores, 'columns': X.columns}) \
        .sort_values('scores', ascending=False)
    plt.figure(figsize=(10, 20))
    sns.barplot(data=scores_df, x='scores', y='columns', color='blue')
    plt.grid(True)
    plt.title(f'Feature {method} score')
    plt.xlabel(f'{method.capitalize()} score ({metric_label})')
    plt.ylabel('')
    plt.show()
