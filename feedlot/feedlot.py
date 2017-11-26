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

result = get_evaluatable().create_from(PrologString(temperature_model)).evaluate()
print result