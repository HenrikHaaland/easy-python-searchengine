a = [1, 2, 3]
a.append(4)

for tall in a:
    print(tall)

var1 = "hei på deg"

print(var1.split(" "))

for word in var1.split(" "):
    print(word)
    if word == "hei":
        print("ordet er i teksten")
    else:
        print("ordet er ikke i teksten")