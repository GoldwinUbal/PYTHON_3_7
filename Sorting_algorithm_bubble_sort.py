# Assessment 3.7: Sorting Algorithms
# Name: Goldwin Alcover Ubal
# Sorting Method: Bubble Sort

full_name = "Goldwin Alcover Ubal"

# Create the unsorted array.
# Convert letters to lowercase, ignore spaces/symbols, and remove duplicates.
unsorted_array = []

for character in full_name.lower():
    if character.isalpha() and character not in unsorted_array:
        unsorted_array.append(character)

# Copy the unsorted array so the original remains unchanged.
sorted_array = unsorted_array.copy()

# Sort the array alphabetically using Bubble Sort.
for i in range(len(sorted_array)):
    for j in range(0, len(sorted_array) - i - 1):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

# Display both arrays.
print("Full Name:", full_name)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
