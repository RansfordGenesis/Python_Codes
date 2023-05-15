class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validPointIndex = []
        manhattan = []
        for b in points:
            if b[0] == x or b[1] == y:
                validPointIndex.append(points.index(b))
        for c in validPointIndex:
            manhattan.append(abs(x - points[c][0]) + abs(y - points[c][1]))           
        return validPointIndex[manhattan.index(min(manhattan))] if manhattan else -1
