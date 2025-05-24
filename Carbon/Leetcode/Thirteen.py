class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        Letters_to_int = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        total = 0
        i = 0
        while i < len(s):
            key = s[i:i + 2]
            if i < len(s) - 1 and key in Letters_to_int:
                total += Letters_to_int[key]
                print("Adding two letters:", key, "Total:", total)
                i += 2
            else:
                total += Letters_to_int[s[i]]
                print("Adding one letter:", s[i], "Total:", total)
                i += 1

        return int(total)


main = __name__ == "__main__"
if main:
    solution = Solution()

    s = "LVIII"
    print(solution.romanToInt(s))