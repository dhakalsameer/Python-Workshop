# 1. Remove duplicate elements from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
print("\n")

# 2. Find common elements from two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)
print("\n")

# 3. Separate even and odd numbers
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)
print("\n")

# 4. Student with highest marks
students = {
    "Ram": 85,
    "Sita": 92,
    "Hari": 78
}
top_student = max(students, key=students.get)
print("Highest marks:", top_student)
print("\n")

# 5. Increase all prices by 10%
items = {
    "Pen": 10,
    "Book": 100,
    "Bag": 500
}
for item in items:
    items[item] += items[item] * 0.10

print(items)
print("\n")


# 6. Count character frequency
text = "hello"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
print("\n")


# 7. Find largest and smallest number
def find_min_max(numbers):
    return min(numbers), max(numbers)

nums = [10, 5, 20, 2]
small, large = find_min_max(nums)
print("Smallest:", small)
print("Largest:", large)
print("\n")


# 8. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("education"))
print("\n")


# 9. Check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print("\n")


# 10. Word length dictionary
def word_length(words):
    result = {}
    for word in words:
        result[word] = len(word)
    return result

words = ["apple", "banana", "cat"]
print(word_length(words))
print("\n")
