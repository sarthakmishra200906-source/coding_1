
# 1. Set Creation & Duplicate Removal
# Sets automatically eliminate duplicate values and have no fixed order
print("1. Creation & Unique Values:")
numbers = {1, 2, 3, 4, 2, 1, 5}
print("Original elements with duplicates turned into set:", numbers)
print("-" * 40)


# 2. Adding Elements
# Use .add() for single items and .update() for multiple items (lists, tuples, sets)
print("2. Adding Elements:")
my_set = {10, 20, 30}
my_set.add(40)               # Adds a single element
my_set.update([50, 60, 10])  # Adds multiple elements (ignores duplicate 10)
print("After adding elements:", my_set)
print("-" * 40)


# 3. Removing Elements
# .remove() throws an error if the item isn't there; .discard() does not.
print("3. Removing Elements:")
my_set.remove(20)   # Removes 20 safely
my_set.discard(99)  # 99 is not in set, but discard() won't throw an error
print("After removal:", my_set)
print("-" * 40)


# 4. Set Mathematical Operations (Union)
# Combines all unique elements from both sets
print("4. Union Operation:")
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_result = set_a | set_b  # or set_a.union(set_b)
print("Union of A and B:", union_result)
print("-" * 40)


# 5. Set Mathematical Operations (Intersection)
# Finds elements present in BOTH sets
print("5. Intersection Operation:")
intersection_result = set_a & set_b  # or set_a.intersection(set_b)
print("Intersection of A and B:", intersection_result)
print("-" * 40)


# 6. Set Mathematical Operations (Difference)
# Finds elements that are in the first set but NOT in the second
print("6. Difference Operation:")
diff_result = set_a - set_b  # Elements in A that are not in B
print("Difference (A - B):", diff_result)
print("-" * 40)


# 7. Set Mathematical Operations (Symmetric Difference)
# Elements in either set A or set B, but NOT in both
print("7. Symmetric Difference:")
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print("Symmetric Difference (A ^ B):", sym_diff)
print("-" * 40)


# 8. Membership Testing
# Checking if an item exists is extremely fast in sets (`O(1)` time complexity)
print("8. Membership Testing:")
fruits = {"apple", "banana", "cherry"}
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 'grape' in fruits?", "grape" in fruits)
print("-" * 40)


# 9. Subset and Superset Checks
print("9. Subset and Superset:")
sub = {1, 2}
main_set = {1, 2, 3, 4, 5}
print("Is 'sub' a subset of 'main_set'?", sub.issubset(main_set))
print("Is 'main_set' a superset of 'sub'?", main_set.issuperset(sub))
print("-" * 40)


# 10. Practical Trick: Removing Duplicates from a List
# Converting a list to a set and back to a list is the fastest way to drop duplicates!
print("10. Practical Application (List to Set Conversion):")
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicate_list))
print("Original list with duplicates:", duplicate_list)
print("Converted unique list:", unique_list)
print("=" * 40)