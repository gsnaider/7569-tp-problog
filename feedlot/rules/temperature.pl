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