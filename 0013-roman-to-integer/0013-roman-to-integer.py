class Solution:
    def romanToInt(self, s: str) -> int:
        li = list(reversed(s))
        prev = 0
        res = 0
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in li:
            if i in roman_values:
                val = roman_values[i]
                if val >= res or val>=prev:
                    res+=val
                else:
                    res -= val
                prev = roman_values[i]
        return res