a = 4
b = 2

c = a / b
print(c)

celsius_temperature = 33

if celsius_temperature > 30:
    print("Starting sprinklers")
    print("Staring pump")
else:
    print("Waiting...")
print("End")

if celsius_temperature < 5:
    print("Starting heating system")
elif celsius_temperature > 32:
    print("Staring AC")

weather_condition = "ideal conditions" if 20 < celsius_temperature < 28 else "NOT"
print(weather_condition)

interior_temperature = 18
while interior_temperature < 24:
    print("Heating...")
    interior_temperature += 2

result = 1 / 3
value = 0.33
if abs(result - value) < 0.01:
    print("Works")

for s in "abcd":
    print(s)
print()

for i in range(1, 4, 2):
    print(i)

x = [s.upper() for s in "abcd"]
print(x)

for i in range(4):
    pass
else:
    print("Break was not executed")