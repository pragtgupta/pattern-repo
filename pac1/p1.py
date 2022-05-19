# initializing lists
test_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
insert_list = ["h", "i", "j"]

# initializing position
pos = 3

# printing original list
print("The original list is : " + str(test_list))

# printing insert list
print("The list to be inserted is : " + str(insert_list))

# using list slicing
# to insert one list in another
test_list[pos:pos] = insert_list

# printing result
print("The list after insertion is : " + str(test_list))