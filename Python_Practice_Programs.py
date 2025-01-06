
# Python Programs for Practice

# 1. Reverse a String
def reverse_string(input_str):
    return input_str[::-1]

input_str = "HelloWorld"
print("Original String:", input_str)
print("Reversed String:", reverse_string(input_str))


# 2. Find Duplicates in a List
def find_duplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

nums = [1, 2, 3, 4, 2, 5, 6, 3]
print("Duplicate elements:", find_duplicates(nums))


# 3. Sort a List in Ascending Order
nums = [5, 3, 8, 6, 2]
nums.sort()
print("Sorted List:", nums)


# 4. Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

input_str = "madam"
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")


# 5. Find the Maximum and Minimum in a List
nums = [12, 5, 7, 3, 19, 8]
print("Maximum:", max(nums))
print("Minimum:", min(nums))


# 6. Count Vowels and Consonants in a String
def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

input_str = "HelloWorld"
vowels, consonants = count_vowels_consonants(input_str)
print("Vowels:", vowels)
print("Consonants:", consonants)


# 7. Remove Duplicates from a List
nums = [1, 2, 3, 2, 4, 5, 5, 6]
unique_nums = list(set(nums))
print("List without duplicates:", unique_nums)


# 8. Merge Two Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = sorted(list1 + list2)
print("Merged and Sorted List:", merged_list)


# 9. Find the Second Largest Element in a List
nums = [10, 20, 4, 45, 99]
nums = sorted(set(nums))  # Remove duplicates and sort
print("Second Largest Element:", nums[-2])


# 10. Count Occurrences of Each Character in a String
from collections import Counter

input_str = "programming"
char_count = Counter(input_str)
print("Character Count:", char_count)


# 11. Check if Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

str1 = "listen"
str2 = "silent"
if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 12. Find Factorial of a Number Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = 5
print("Factorial of", number, "is:", factorial(number))


# 13. Fibonacci Series Using Iteration
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)


# 14. Check if a Number is Prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 29
print(f"{number} is prime.") if is_prime(number) else print(f"{number} is not prime.")


# 15. Reverse a List In-Place
nums = [1, 2, 3, 4, 5]
nums.reverse()
print("Reversed List:", nums)


# 16. Generate a Pyramid Pattern of Numbers
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + " ".join(str(x) for x in range(1, i + 1)))


# 17. Find GCD (Greatest Common Divisor) of Two Numbers
import math

num1, num2 = 56, 98
print("GCD of", num1, "and", num2, "is:", math.gcd(num1, num2))


# 18. Count Positive and Negative Numbers in a List
nums = [-1, 2, -3, 4, 5, -6]
positive_count = len([num for num in nums if num > 0])
negative_count = len([num for num in nums if num < 0])
print("Positive Numbers:", positive_count)
print("Negative Numbers:", negative_count)


# 19. Find the Length of the Longest Word in a Sentence
sentence = "Python is a versatile programming language"
longest_word = max(sentence.split(), key=len)
print("Longest Word:", longest_word)
print("Length:", len(longest_word))


# 20. Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

nums = [5, 1, 4, 2, 8]
bubble_sort(nums)
print("Sorted List:", nums)
