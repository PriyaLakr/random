info = [("Pri", 35), ("Ada", 50), ("Meg", 27), ("Sar", 37)]

# sorting list from oldest "Ada" to youngest "Meg"
list(reversed(sorted(info, key=lambda x: x[1])))
