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