# Initialize a sample list of numbers (with duplicates)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]
print("Original List:", my_list)


# 1. Sum and Average of the list
total_sum = 0
for i in my_list:
    total_sum += i
print("The sum of the list is:", total_sum)
print("The average of the list is:", total_sum / len(my_list))


# 2. Largest and Smallest element in the list (without max() or min())
largest = my_list[0]
smallest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("The largest element in the list is:", largest)
print("The smallest element in the list is:", smallest)


# 3. Second largest element in the list
# We first find the largest, then look for the highest number strictly less than 'largest'
second_largest = -1
for i in my_list:
    if i > second_largest and i < largest:
        second_largest = i
print("The second largest element in the list is:", second_largest)


# 4. Remove duplicates from the list
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print("The list with duplicates removed is:", unique_list)


# 5. Merge and sort two lists manually (Bubble Sort)
list1 = [1, 2, 11, 8, 5]
list2 = [6, 7, 11, 9, 10]

merged_list = list1 + list2  # Combine lists

# Manual sort using nested loops
n = len(merged_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if merged_list[j] > merged_list[j + 1]:
            merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

print("The merged and sorted list (manual):", merged_list)

# Alternatively, using Python's built-in sorted() function
merged_list_sorted = sorted(list1 + list2)
print("The merged and sorted list using sorted():", merged_list_sorted)


# 6. Separate Even and Odd numbers into different lists (Fixed: defined outside loop!)
even_list = []
odd_list = []
for i in my_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("The odd list is:", odd_list)
print("The even list is:", even_list)


# 7. Check if numbers in a list are palindromes
palindrome_list = [1234543, 12321, 1234321, 1234567]
for i in palindrome_list:
    # Convert number to string and check if it reads the same backward (using [::-1])
    if str(i) == str(i)[::-1]:
        print(i, "is a palindrome")
    else:
        print(i, "is not a palindrome")


# 8. List Intersection (Find elements present in both list1 and list2)
print("Common elements in list1 and list2:")
for i in list1:
    if i in list2:
        print(i, "is present in both lists")


# 9. Frequency of elements (using count method uniquely)
print("Element Frequencies:")
seen_freq = []
for i in my_list:
    if i not in seen_freq:
        seen_freq.append(i)
        print(f"The frequency of {i} in the list is: {my_list.count(i)}")