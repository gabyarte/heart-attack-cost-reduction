# UPM Master's in Data Science: Data Process project (II)

## Collaborators
* Elisa Marson ([@elisa98mars](https://github.com/elisa98mars))
* Pablo Bande Girón-Sánchez ([@pbande](https://github.com/pbande))
* Gabriela Argüelles Terrón ([@gabyarte](https://github.com/gabyarte))

## Assigment details
Heart attacks are among the most prevalent chronic diseases in the world, impacting millions of people each year and exerting a significant financial burden on the economy. The buildup of plaques inside larger coronary arteries, molecular changes associated with aging, chronic inflammation, high blood pressure, and diabetes are all causes of and risk factors for heart disease.

A national healthcare system has done a telephone survey asking people some life habits and health conditions. The results of the survey can be found in the dataset whose features are described in the annex. The goal is to reduce the costs associated to heart attacks in the national healthcare system by a 20%.

We know that we can reduce the risk of suffering a heart attack in a person who is prone to it by a 75% if we settle up a specific lifestyle modification plan for that person. The cost of the treating a person who has suffered a heart attack is of €50,000 in average, while the customized plan for a person costs €1,000. The estimation is that 85% of the people who is offered the plan would accept it, but not all of them will adhere to the plan properly.

Then, you need to do a cost analysis to check the percentage of adherence (from those people who has already accepted the prevention plan) we need to obtain to achieve our goal.

## Business goals
* Reduce the costs associated to heart attacks in the national healthcare system by a 20%

## Data mining goals
* Recognize patterns on the health habits of people
* Predict if the probability of a person having a heart attack or disease
* Select threshold for the percentage of adherence to achieve business goal

## Scope

**Assumptions**:
* 85% of the people who is offered the plan would accept it
* Treating a person who has suffered a heart attack is of €50,000 in average, while the customized plan for a person costs €1,000
* The people who already had a heart attack haven't changed their life style after it

## Next steps
1. Probabilistic classification algorithm (e.g. `Logistic Regression`, `DiscriminantAnalysis`) with target variable `HeartDiseaseorAttack`
2. Select threshold to find people that we are going to offer the plan
3. Randomly apply assumption that 85% of people will accept the plan
4. Select the minimum percentage of adherence to the plan to fulfill business goal


