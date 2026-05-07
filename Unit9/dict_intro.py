import json

# Recap lists
int_value = 40
float_value = 3.14
string_value = "Alice"

# Combine the single values in a list
our_list = [int_value, float_value, string_value]
print(our_list)

# Dictionary
our_dict = {"age": 23, "name": "Alice", "id": 1}

print(our_dict)

# Access individual fields by key
print(our_dict["age"])

# Store our dict to disk
with open("./Unit9/our_dict.json", "w") as f:
    json.dump(our_dict, f)

# Load json from disk
with open("./Unit9/student.json", "r") as f:
    student = json.load(f)
print(student)
