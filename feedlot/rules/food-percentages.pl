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