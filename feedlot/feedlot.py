from problog.program import PrologString
from problog import get_evaluatable
import re

#TODO: Move model strings to external files.

temperature_model = """
temperatureFactor(cold,1.05).
temperatureFactor(hot,0.95).
temperatureFactor(normal,1.00).

cold :- temperature(T), T<20.
hot :- temperature(T), T>28.
normal :- \+cold, \+hot.

temperatureFactor(F) :- cold, temperatureFactor(cold,FC), F is FC.
temperatureFactor(F) :- hot, temperatureFactor(hot,FH), F is FH.
temperatureFactor(F) :- normal, temperatureFactor(normal,FN), F is FN.

temperature(%s).

query(temperatureFactor(F)).
"""

dry_food_model = """
dryFoodPercentage(day1, 0.01).
dryFoodPercentage(day6, 0.02).
dryFoodPercentage(day15, 0.03).
dryFoodPercentage(day26, 0.029).

day1 :- day(D), D<6.
day6 :- day(D), D>=6, D<15.
day15 :- day(D), D>=15, D<26.
day26 :- day(D), D>=26.

dryFoodPercentage(P) :- day1, dryFoodPercentage(day1, P1), P is P1.
dryFoodPercentage(P) :- day6, dryFoodPercentage(day6, P6), P is P6.
dryFoodPercentage(P) :- day15, dryFoodPercentage(day15, P15), P is P15.
dryFoodPercentage(P) :- day26, dryFoodPercentage(day26, P26), P is P26.

day(%s).

query(dryFoodPercentage(P)).
"""

food_percentages_model = """
sorghumPercentage(day1, 0.48).
sorghumPercentage(day11, 0.37).
sorghumPercentage(day22, 0.265).

cornPercentage(day1, 0.38).
cornPercentage(day11, 0.49).
cornPercentage(day22, 0.598).

soyExpellerPercentage(day1, 0.124).
soyExpellerPercentage(day11, 0.1225).
soyExpellerPercentage(day22, 0.12).

mineralPremixPercentage(day1, 0.016).
mineralPremixPercentage(day11, 0.0175).
mineralPremixPercentage(day22, 0.017).

day1 :- day(D), D<11.
day11 :- day(D), D>=11, D<22.
day22 :- day(D), D>=22.

sorghumPercentage(P) :- day1, sorghumPercentage(day1, P1), P is P1.
sorghumPercentage(P) :- day11, sorghumPercentage(day11, P11), P is P11.
sorghumPercentage(P) :- day22, sorghumPercentage(day22, P22), P is P22.

cornPercentage(P) :- day1, cornPercentage(day1, P1), P is P1.
cornPercentage(P) :- day11, cornPercentage(day11, P11), P is P11.
cornPercentage(P) :- day22, cornPercentage(day22, P22), P is P22.

soyExpellerPercentage(P) :- day1, soyExpellerPercentage(day1, P1), P is P1.
soyExpellerPercentage(P) :- day11, soyExpellerPercentage(day11, P11), P is P11.
soyExpellerPercentage(P) :- day22, soyExpellerPercentage(day22, P22), P is P22.

mineralPremixPercentage(P) :- day1, mineralPremixPercentage(day1, P1), P is P1.
mineralPremixPercentage(P) :- day11, mineralPremixPercentage(day11, P11), P is P11.
mineralPremixPercentage(P) :- day22, mineralPremixPercentage(day22, P22), P is P22.

day(%s).

query(sorghumPercentage(P)).
query(cornPercentage(P)).
query(soyExpellerPercentage(P)).
query(mineralPremixPercentage(P)).
"""


def evaluate_model(model):
    result = get_evaluatable().create_from(PrologString(model)).evaluate()
    result_dict = {}
    for name, value in result.items():
        result_dict[str(name)] = value
    return result_dict


def format_model(model, value):
    return model % value


def format_result(results):
    results_as_dict = {}
    for key in results.keys():
        search = re.search('(\w+)\(([0-9\.]+)\)', key)
        if search:
            results_as_dict[search.group(1)] = float(search.group(2))
        else:
            print "Error: Result did not match."
    return results_as_dict

#TODO: Read data from console
temperature = 30
day = 50

temperatures = evaluate_model(format_model(temperature_model, temperature))
print format_result(temperatures)

dry_food = evaluate_model(format_model(dry_food_model, day))
print format_result(dry_food)

food_percentages = evaluate_model(format_model(food_percentages_model, day))
print format_result(food_percentages)



