# 🌟 Unpacking Iterables in Python

# 1. Unpacking in Function Arguments
def add(a, b, c):
    print("Sum:", a + b + c)

nums = [1, 2, 3]
add(*nums)  # Unpacks list into separate arguments


# 2. Unpacking in Variable Assignment
a, b, *rest = [10, 20, 30, 40, 50]
print("a:", a)       # 10
print("b:", b)       # 20
print("rest:", rest) # [30, 40, 50]


# 3. Unpacking Multiple Lists
list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2]
print("Combined list:", combined)  # [1, 2, 3, 4]


# 4. Unpacking a String
letters = [*"ABC"]
print("Letters:", letters)  # ['A', 'B', 'C']


# 5. Using * to Ignore Values
first, *_, last = [10, 20, 30, 40, 50]
print("First:", first)  # 10
print("Last:", last)    # 50


# 6. Bonus: Unpacking Dictionaries with **
dict1 = {'a': 1}
dict2 = {'b': 2}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)  # {'a': 1, 'b': 2}