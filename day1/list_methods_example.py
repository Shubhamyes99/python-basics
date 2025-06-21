friends = ["Shubham", "Mayur", "Swaraj", "Sarang"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[0])
print(friends[-3])
print(friends[-2])
print(friends[-1])


# Common Python list methods

# append() - Adds item to the end
friends.append("Sarang")
print(friends)

# insert(index, value) - Adds item at specific index
friends.insert(1, "Aditya")
print(friends)

# remove(value) - Removes first matching value
friends.remove("Mayur")
print(friends)

# pop() - Removes last item by default
friends.pop()
print(friends)

# index(value) - Finds index of value
print(friends.index("Swaraj"))

# count(value) - Counts how many times a value appears
friends.append("Shubham")
print(friends.count("Shubham"))

# sort() - Sorts list alphabetically
friends.sort()
print(friends)

# reverse() - Reverses current order
friends.reverse()
print(friends)

# clear() - Empties the list
friends.clear()
print(friends)



# Common Python list methods

friends = ["Shubham", "Mayur", "Swaraj"]

# append() - Adds item to the end
friends.append("Sarang")
print("After append:", friends)

# insert(index, value) - Adds item at specific index
friends.insert(1, "Aditya")
print("After insert at index 1:", friends)

# remove(value) - Removes first matching value
friends.remove("Mayur")
print("After removing 'Mayur':", friends)

# pop() - Removes last item by default
friends.pop()
print("After pop():", friends)

# index(value) - Finds index of value
print("Index of Swaraj:", friends.index("Swaraj"))

# count(value) - Counts how many times a value appears
friends.append("Shubham")
print("Count of 'Shubham':", friends.count("Shubham"))

# sort() - Sorts list alphabetically
friends.sort()
print("After sort:", friends)

# reverse() - Reverses current order
friends.reverse()
print("After reverse:", friends)

# clear() - Empties the list
friends.clear()
print("After clear():", friends)
