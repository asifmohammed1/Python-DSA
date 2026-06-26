class PythonPractice:

    # Question 1
    def reverse_string(self, text):
        return text[::-1]

    # Question 2
    def is_palindrome(self, text):
        return text == text[::-1]

    # Question 3
    def count_vowels(self, text):
        count = 0
        for char in text.lower():
            if char in "aeiou":
                count += 1
        return count

    # Question 4
    def largest_number(self, nums):
        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num
        return largest

    # Question 5
    def second_largest(self, nums):
        unique = list(set(nums))
        unique.sort()
        return unique[-2]

    # Question 6
    def remove_duplicates(self, nums):
        result = []
        for num in nums:
            if num not in result:
                result.append(num)
        return result

    # Question 7
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    # Question 8
    def fibonacci(self, n):
        series = []
        a = 0
        b = 1
        for i in range(n):
            series.append(a)
            a, b = b, a + b
        return series

    # Question 9
    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    # Question 10
    def char_frequency(self, text):
        frequency = {}
        for char in text:
            frequency[char] = frequency.get(char, 0) + 1
        return frequency

    # Question 11
    def valid_anagram(self, text1, text2):
        return sorted(text1) == sorted(text2)

    # Question 12
    def longest_word(self, sentence):
        words = sentence.split()
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest

    # Question 13
    def count_words(self, sentence):
        words = sentence.split()
        return len(words)

    # Question 14
    def reverse_words(self, sentence):
        words = sentence.split()
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return " ".join(reversed_words)

    # Question 15
    def missing_number(self, nums):
        n = len(nums) + 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # Question 16
    def find_duplicates(self, nums):
        seen = set()
        duplicates = []
        for num in nums:
            if num in seen and num not in duplicates:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates

    # Question 17
    def common_elements(self, list1, list2):
        common = []
        for item in list1:
            if item in list2:
                common.append(item)
        return common

    # Question 18
    def two_sum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[nums[i]] = i

    # Question 19
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    # Question 20
    def rotate_array(self, nums, k):
        k = k % len(nums)
        return nums[-k:] + nums[:-k]

obj = PythonPractice()

print(obj.reverse_string("hello"))
print(obj.is_palindrome("madam"))
print(obj.count_vowels("python programming"))
print(obj.largest_number([10, 50, 30, 80, 20]))
print(obj.second_largest([10, 20, 50, 40]))
print(obj.remove_duplicates([1, 2, 2, 3, 4, 4]))
print(obj.is_prime(13))
print(obj.fibonacci(5))
print(obj.factorial(5))
print(obj.char_frequency("hello"))
print(obj.valid_anagram("listen", "silent"))
print(obj.longest_word("Python is very easy language"))
print(obj.count_words("Python is easy to learn"))
print(obj.reverse_words("Hello World"))
print(obj.missing_number([1,2,3,5]))
print(obj.find_duplicates([1,2,3,2,4,1]))
print(obj.common_elements([1,2,3,4],[3,4,5,6]))
print(obj.two_sum([2,7,11,15],9))
print(obj.bubble_sort([10,50,30,80,20]))
print(obj.rotate_array([1, 2, 3, 4, 5], 2))
