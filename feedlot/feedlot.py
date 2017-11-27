from problog.program import PrologString
from problog import get_evaluatable
import re

# TODO: Move model strings to external files.

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

weight_in_dry_food_model = """
weightInDryFoodPercentage(day1, 0.01).
weightInDryFoodPercentage(day6, 0.02).
weightInDryFoodPercentage(day15, 0.03).
weightInDryFoodPercentage(day26, 0.029).

day1 :- day(D), D<6.
day6 :- day(D), D>=6, D<15.
day15 :- day(D), D>=15, D<26.
day26 :- day(D), D>=26.

weightInDryFoodPercentage(P) :- day1, weightInDryFoodPercentage(day1, P1), P is P1.
weightInDryFoodPercentage(P) :- day6, weightInDryFoodPercentage(day6, P6), P is P6.
weightInDryFoodPercentage(P) :- day15, weightInDryFoodPercentage(day15, P15), P is P15.
weightInDryFoodPercentage(P) :- day26, weightInDryFoodPercentage(day26, P26), P is P26.

day(%s).

query(weightInDryFoodPercentage(P)).
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

dryFoodPercentage(day1, 0.62).
dryFoodPercentage(day11, 0.67).
dryFoodPercentage(day22, 0.73).

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

dryFoodPercentage(P) :- day1, dryFoodPercentage(day1, P1), P is P1.
dryFoodPercentage(P) :- day11, dryFoodPercentage(day11, P11), P is P11.
dryFoodPercentage(P) :- day22, dryFoodPercentage(day22, P22), P is P22.

day(%s).

query(sorghumPercentage(P)).
query(cornPercentage(P)).
query(soyExpellerPercentage(P)).
query(mineralPremixPercentage(P)).
query(dryFoodPercentage(P)).
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


def calculate_current_weight(initial_weight):
    if (day > 25):
        return initial_weight + (day - 25) * 1.2
    else:
        return initial_weight


def calculate_dry_food_kilograms(current_weight, weight_in_dry_food_percentage, heads, temperatures_factor):
    return current_weight * weight_in_dry_food_percentage * heads * temperatures_factor


def round(f):
    return ("%.2f" % f)


# TODO: Read data from console
heads = 50
day = 18
initial_weight = 225
temperature = 26

current_weight = calculate_current_weight(initial_weight)

temperatures_result = format_result(evaluate_model(format_model(temperature_model, temperature)))
weight_in_dry_food_result = format_result(evaluate_model(format_model(weight_in_dry_food_model, day)))
food_percentages_result = format_result(evaluate_model(format_model(food_percentages_model, day)))

dry_food_kilograms = calculate_dry_food_kilograms(current_weight,
                                                  weight_in_dry_food_result.get('weightInDryFoodPercentage'), heads,
                                                  temperatures_result.get('temperatureFactor'))
dry_food_factor = food_percentages_result.get('dryFoodPercentage')
dry_food_percentage = dry_food_factor * 100

sorghum_kilograms = food_percentages_result.get('sorghumPercentage') * dry_food_kilograms
sorghum_percentage = food_percentages_result.get('sorghumPercentage') * 100

corn_kilograms = food_percentages_result.get('cornPercentage') * dry_food_kilograms
corn_percentage = food_percentages_result.get('cornPercentage') * 100

soy_expeller_kilograms = food_percentages_result.get('soyExpellerPercentage') * dry_food_kilograms
soy_expeller_percentage = food_percentages_result.get('soyExpellerPercentage') * 100

mineral_premix_kilograms = food_percentages_result.get('mineralPremixPercentage') * dry_food_kilograms
mineral_premix_percentage = food_percentages_result.get('mineralPremixPercentage') * 100

water = (1 - dry_food_factor) * (dry_food_kilograms / dry_food_factor)

print "La racion en materia seca de hoy es de %s kg (%s %%)" % (round(dry_food_kilograms), round(dry_food_percentage))
print "Dividida en:"
print "Silo sorgo:  %s kg (%s %%)" % (round(sorghum_kilograms), round(sorghum_percentage))
print "Maiz:  %s kg (%s %%)" % (round(corn_kilograms), round(corn_percentage))
print "Expeller de Soja:  %s kg (%s %%)" % (round(soy_expeller_kilograms), round(soy_expeller_percentage))
print "Premezcla Mineral:  %s kg (%s %%)" % (round(mineral_premix_kilograms), round(mineral_premix_percentage))
print "A la materia seca hay que agregarle %s litros de agua" % round(water)
