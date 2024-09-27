tuples = (1,2,3,4,5,6,7,8,9)

print(tuples[5])

stringTuple = ("cat","cow","dog")

print(stringTuple[2])

"adding items to a tuple"
"by concatinating"
t = tuples + ("cow","goat")
print(t)
print(tuples)

"comp(letely changing the original tuple"
l = list(tuples)
l.insert(0,100)
print(l)

x = tuple(l)
print(l)
print(type(l))
print(len(x))

"removing an item from a tuple"
"using slicing"
print(x[4:5])
print(x)

"turning it to a list first"
s = list(x)
s.remove(100)
print(s)

x = tuple(s)
print(x)
print(type(x))