class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for each in details:
            if int(each[11:13]) > 60:
                count += 1
        return count
