# in a set it removes the duplicates
# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# my_set.add(11)
# print(my_set)

# creating a set out of a list
# my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# # only shows the difference between the two sets
# print(my_set.difference(your_set))

# # discards value from the set
# print(my_set.discard(5))
# print(my_set)

# updates the set with the differences between the two sets
# print(my_set.difference_update(your_set))
# print(my_set)

# prints the union of the two sets
# print(my_set.intersection(your_set))
# does the same thing as intersection
# print(my_set & your_set)

# checks if the two sets have any common elements
# print(my_set.isdisjoint(your_set))

# checks if the set is a subset of the other set (all elements in the set are in the other set)
# print(my_set.issubset(your_set))

# combines the two sets
# print(my_set.union(your_set))
# does the same thing as union
# print(my_set | your_set)

# checks if the set is in the other set
# print(my_set.issubset(your_set))

# checks if the other set is in the set
print(my_set.issuperset(your_set))
