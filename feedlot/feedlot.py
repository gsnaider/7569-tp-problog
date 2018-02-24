from problog.program import PrologString
from problog import get_evaluatable
import re

TEMPERATURE_RULES_PATH = "rules/temperature.pl"
WEIGHT_IN_DRY_FOOD_RULES_PATH = "rules/weight-in-dry-food.pl"
FOOD_PERCENTAGES_RULES_PATH = "rules/food-percentages.pl"

def evaluate_model(model):
    result = get_evaluatable().create_from(PrologString(model)).evaluate()
    result_dict = {}
    for name, value in result.items():
        result_dict[str(name)] = value
    return result_dict


def format_rules(rules, value):
    return rules % value


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


def read_rules_files():
    rule_file_paths = [TEMPERATURE_RULES_PATH, WEIGHT_IN_DRY_FOOD_RULES_PATH, FOOD_PERCENTAGES_RULES_PATH]
    rules = []
    for path in rule_file_paths:
        file = open(path, "r")
        rules.append(file.read())
    return tuple(rules)


def read_from_console(prompt, conversion_function):
    val = None
    while(val == None):
        input = raw_input(prompt)
        try:
            val = conversion_function(input)
        except ValueError:
            print("Tipo de dato invalido.")
    return val



def read_values_from_console():
    heads = read_from_console("Ingrese cantidad de ganado (cabezas):", int)
    while (heads < 1):
        print "Valor invalido."
        heads = read_from_console("Ingrese cantidad de ganado (cabezas):", int)

    day = read_from_console("Ingrese el dia actual del rodeo:", int)
    while (day < 1):
        print "Valor invalido."
        day = read_from_console("Ingrese el dia actual del rodeo:", int)

    initial_weight = read_from_console("Ingrese el peso inicial del ganado:", float)
    while (initial_weight <= 0):
        print "Valor invalido."
        initial_weight = read_from_console("Ingrese el peso inicial del ganado:", float)

    temperature = read_from_console("Ingrese la temperatura actual:", float)

    return (heads, day, initial_weight, temperature)


(heads, day, initial_weight, temperature) = read_values_from_console()

current_weight = calculate_current_weight(initial_weight)

(temperature_rules, weight_in_dry_food_rules, food_percentages_rules) = read_rules_files()
temperatures_result = format_result(evaluate_model(format_rules(temperature_rules, temperature)))
weight_in_dry_food_result = format_result(evaluate_model(format_rules(weight_in_dry_food_rules, day)))
food_percentages_result = format_result(evaluate_model(format_rules(food_percentages_rules, day)))

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
