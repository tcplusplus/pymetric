# pymetric
A static typed metric system representation

A testing platform to create static typing in python

## Examples
```
distance = Distance(unit=6.5, metric=M)
new_distance = distance + Distance(unit=2, metric=KM)

speed = new_distance / Time(34, Sec)
# typechecker will know that speed is of type speed
```

## Goal
This library does compile-time checking that the parameters are used correctly and can validate your equations that
by checking the types of the metric.

It is however not computational efficient as for each metric a class is created. Therefore it is not recommended
for heavy number crunching.

Eg: creating a metric such as `Speed(4.0, Mps)` is around 60x times slower then creating the float `4.0`

Adding together 2 metrics like `Speed(4.0, Mps)` and `Speed(5.0, Mps)` is around 90x slower then adding `4.0` and `5.0`