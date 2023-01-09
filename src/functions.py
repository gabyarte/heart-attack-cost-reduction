import numpy as np


def get_population_amount(df, prob_column, target_column, threshold=None):
    return (
        df[df[target_column].eq(1)].shape[0]
        if threshold is None 
        else df[df[prob_column].ge(threshold)]
    )


def get_populations(df, prob_column, target_column, acceptance_percentage,
                    adherence_percentage=None, threshold=None):
    # get amount of people
    population_amount = get_population_amount(
        df, prob_column, target_column, threshold)

    # population who is going to be offered the plan is the most vulnerable one
    offer_population = df.sort_values(prob_column, ascending=False)\
                         .iloc[:population_amount]
    # randomly select population who will accept the plan based on
    # 85% assumption
    acceptance_population = offer_population.sample(frac=acceptance_percentage)
    adherence_population = None
    if adherence_percentage:
        adherence_population = acceptance_population.sample(
            frac=adherence_percentage)
    return (offer_population, acceptance_population, adherence_population)


def cost_analysis(df, prob_column, target_column, reduction_goal,
                  acceptance_percentage, pre_cost, post_cost, threshold=None):
    # get amount of people
    population_amount = get_population_amount(
        df, prob_column, target_column, threshold)
    print(f'{population_amount=}')
    # get baseline cost to reduce with the plan
    baseline_cost = population_amount * post_cost
    print(f'{baseline_cost=}')
    # get reduced cost
    reduced_cost = baseline_cost * reduction_goal
    print(f'{reduced_cost=}')
    # get amount of people that will accept the plan
    accept_amount = population_amount * acceptance_percentage
    # amount of people that should adhere the plan in order to achieve the goal
    adherence_amount = (baseline_cost - reduced_cost) / (post_cost - pre_cost)
    print(f'{adherence_amount=}')
    # get percentage of adherance
    adherence_percentage = adherence_amount / accept_amount
    print(f'{adherence_percentage=}')
    return adherence_percentage, reduced_cost


def risk_analysis(offer_df, adherance_df, prob_column, risk_reduction):
    # mean vulnerable population's risk
    mean_baseline_risk = offer_df[prob_column].mean()
    print(f'{mean_baseline_risk=}')
    # reduce vulnerable population's risk
    mean_reduced_risk = np.where(
        offer_df.index.isin(adherance_df.index),
        offer_df[prob_column] * risk_reduction,
        offer_df[prob_column]
    ).mean()
    print(f'{mean_reduced_risk=}')
    return mean_reduced_risk
