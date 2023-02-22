# list is muttable and is slow compared to tuple.

flower = ["Rose", "Sunflower", "Daisy"]

print(flower[1])
print(type(flower))

print(flower)
flower.append("Marigold")
print(flower)

print(flower)
flower.insert(2, "Lotus")
print(flower)

flower.remove("Lotus")
print(flower)

flower.remove(flower[0])
print(flower)

print(len(flower))

flower.pop()
print(flower)

pop_Var = flower.pop()
print(flower)
# we can print the popped element but can't the remove.
print(pop_Var)

# Tuple is used for fixed data and it is faster. Tuple is immutable.
signal = ("red", "yellow", "Green")
print(signal)

print(flower[0], signal[1])

# Dicitionary
class1 = {
    "Name": "shubham",
    "Email": "shubham@gmail.com",
    "Marks": [90, 91, 92, 93, 94],
    "sports":{
        "indoor":"Ludo",
        "outdoor":"Cricket"
    }
}
print(class1)
print(class1["Marks"][1])
print(class1["sports"]["indoor"])
