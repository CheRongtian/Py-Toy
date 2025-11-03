#immutable lists are called tuples
dimensions=(200,50) #dimensions=(200,), tuple with 1 element
print(dimensions[0])
print(dimensions[1])

original_dimensions=(100,50)
for original_dimension in original_dimensions:
    print(original_dimension)

original_dimensions=(300,20,40)
for modified_dimension in original_dimensions:
    print(modified_dimension)