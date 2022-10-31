class Solution:
    def myAtoi(self, s: str) -> int:
        max_num = 2147483647
        min_num = -2147483648
        s = s.strip()
        final = ""
        value = 0
        if len(s) < 1:
            return 0

        if s[0] == "+" or "0" <= s[0] <= "9": 
            s = s.replace("+", "", 1)
            for x in s:
                if x.isdigit():
                    final += x
                    value = int(final) * 1
                else:
                    break
            if value < max_num:
                return value
            else:
                return max_num

        elif s[0] == "-":
            s = s[1:]
            for x in s:
                if x.isdigit():
                    final += x
                    value = int(final) * -1
                else:
                    break
            if value > min_num:
                return value
            else:
                return min_num

        else:
            return 0
