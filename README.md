# pymetric
A static typed metric system representation

A testing platform to craete static typing in python

## Examples
```
distance = Distance(unit=6.5, metric=M)
new_distance = distance + Distance(unit=2, metric=KM)

speed = new_distance / Time(34, Sec)
# typechecker will know that speed is of type speed
```
