from problog.program import PrologString
from problog import get_evaluatable

#Move these constants to the models if possible.
COLD_FACTOR = 1.05
HEAT_FACTOR = 0.95
NORMAL_TEMPERATURE_FACTOR = 1.00

INITIAL_DRY_FOOD_PERCENTAGE = 0.01
DAY_6_DRY_FOOD_PERCENTAGE = 0.02
DAY_15_DRY_FOOD_PERCENTAGE = 0.03
DAY_26_DRY_FOOD_PERCENTAGE = 0.029

INITIAL_SORGHUM_PERCENTAGE = 0.48
DAY_11_SORGHUM_PERCENTAGE = 0.37
DAY_22_SORGHUM_PERCENTAGE = 0.265

INITIAL_CORN_PERCENTAGE = 0.38
DAY_11_CORN_PERCENTAGE = 0.49
DAY_22_CORN_PERCENTAGE = 0.598

INITIAL_SOY_EXPELLER_PERCENTAGE = 0.124
DAY_11_SOY_EXPELLER_PERCENTAGE = 0.1225
DAY_22_SOY_EXPELLER_PERCENTAGE = 0.12

INITIAL_MINERAL_PREMIX_PERCENTAGE = 0.016
DAY_11_MINERAL_PREMIX_PERCENTAGE = 0.0175
DAY_22_MINERAL_PREMIX_PERCENTAGE = 0.017


temperature_model = """
cold :- temperature(T), T<20.
hot :- temperature(T), T>28.
normalTemperature :- \+cold, \+hot.

temperature(10).

query(cold).
query(hot).
query(normalTemperature).
"""

dry_food_model = """
initialDryFood :- day(D), D<6.
day6DryFood :- day(D), D>=6, D<15.
day15DryFood :- day(D), D>=15, D<26.
day26DryFood :- day(D), D>=26.

day(18).

query(initialDryFood).
query(day6DryFood).
query(day15DryFood).
query(day26DryFood).
"""

food_percentages_model = """
initialPercentages :- day(D), D<11.
day11Percentages :- day(D), D>=11, D<22.
day22Percentages :- day(D), D>=22.

day(18).

query(initialPercentages).
query(day11Percentages).
query(day22Percentages).
"""


def evaluate_model(model):
    result = get_evaluatable().create_from(PrologString(model)).evaluate()
    result_dict = {}
    for name, value in result.items():
        result_dict[str(name)] = value
    return result_dict


temperatures = evaluate_model(temperature_model)
print temperatures

dry_food = evaluate_model(dry_food_model)
print dry_food

food_percentages = evaluate_model(food_percentages_model)
print food_percentages



