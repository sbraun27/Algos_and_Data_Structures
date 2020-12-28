array = [10, 3, 7, 5]

print(array)

# Random Indexing: Access the given item based on the passed index

print(array[0])
print(array[3])

print(array[1:3])

print(array[:-1])  # all items except for the last one

array1 = [10.0, 3, "adam", 5]
array1[2] = "Kevin"

array2 = [10, 42, 55, 2, 10]
# Find the maximum item
max = array1[0]
for num in array2:
    if num > max:
        max = num

print(max)
