#Create dictionary of roman numerals and their arabic numeral counterpart
numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = numbers[char]

            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total


roman = "III"

s = Solution()
print(f"The converted value is: {s.romanToInt(roman)}")
