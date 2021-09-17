# pythonic ways!

info = [("Pri", 35), ("Ada", 50), ("Meg", 27), ("Sar", 37)]

# sorting list from oldest "Ada" to youngest "Meg"
list(reversed(sorted(info, key=lambda x: x[1])))


lst = [1,2,3,4]

# map, lambda
list(map( lambda x: x*x, lst ))
> [1, 4, 9, 16]

list(map( lambda x: x/x, lst ))
> [1.0, 1.0, 1.0, 1.0]
