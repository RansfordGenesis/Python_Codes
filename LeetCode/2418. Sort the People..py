class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_dict = sorted(zip(heights, names), reverse=True)
        final = [name for i, name in sorted_dict]
        return final
