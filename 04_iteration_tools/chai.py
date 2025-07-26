my_list = [1,2,3,4,5]
i = iter(my_list)

while True:
    try:
        print(next(i))
    except StopIteration:
        break
print("Iteration complete.")


d = {'a': 1, 'b': 2}

i = iter(d)
while True:
    try:
        key = next(i)
        print(f"Key: {key}, Value: {d[key]}")
    except StopIteration:
        break
print("Iteration over dictionary complete.")

r = range(5)

i = iter(r)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
print("Iteration over range complete.")