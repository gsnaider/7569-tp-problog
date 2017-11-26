from problog.program import PrologString
from problog import get_evaluatable

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



