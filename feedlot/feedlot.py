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


def evaluate_model(model):
    result = get_evaluatable().create_from(PrologString(model)).evaluate()
    result_dict = {}
    for name, value in result.items():
        result_dict[str(name)] = value
    return result_dict


temperatures = evaluate_model(temperature_model)
print temperatures