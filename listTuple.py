import math

#concepte de list
ma_list = list()
ma_list = [1, 2.5, "hello", (0, 5)]
ma_list.append((2, 8))
ma_list.append("welcome")
print(type(ma_list[3]))
print(ma_list)

for i, elt in enumerate(ma_list):
    print("\"{}\" est à la position \"{}\" .".format(elt, i))
    
ma_list.remove("welcome")
ma_list.insert(len(ma_list)-1, "bienvenue")
ma_list.pop()
print("index of 'hello' : {} ".format(ma_list.index("hello")))
ma_list2 = ["coucou", math.pi, math.sqrt(55), ('x','y')]

ma_list.extend(ma_list2)
del(ma_list2)) #delete variable

ma_list.reverse()

print(ma_list)



