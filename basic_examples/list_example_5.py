# range is a function that returns a sequence of numbers can be used to iterate over a list

cost_breakdown = [100.0, 200.0, 50.0, 60.0, 205.0]

my_range = range(5)

print("Indices generated by Range:")

# the indices start at 0 as the first element of a list is at index 0

for i in my_range:
    print(i)


print("Values at indices:")

for i in my_range:
    print(i, cost_breakdown[i])

# we can combine range and len to iterate over the elements of a list more
# suscinctly and avoid hardcoding the length of the list

print("Indices generated by Range and Len:")

for i in range(len(cost_breakdown)):
    print(i, cost_breakdown[i])
