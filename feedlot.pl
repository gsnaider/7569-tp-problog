% Rules:
initialAdaptation :- day(D), D<6.
day6Adaptation :- day(D), D>=6, D<15.
day15Adaptation :- day(D), D>=15, D<26.
day26Adaptation :- day(D), D>=26.

initialPercetages :- day(D), D<11.
day11Percentages :- day(D), D>=11, D<22.
day22Percentages :- day(D), D>=22.

cold :- temperature(T), T<20.
hot :- temperature(T), T>28.
normalTemperature :- \+cold, \+hot.

%Facts
heads(30)
day(18)
initialWeight(225)
temperature(26)

%Queries
query(dryFood)
query(water)

query(sorghum)
query(corn)
query(soyExpeller)
query(mineralPremix)