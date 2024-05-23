class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_work = 0
        min_value = 0
        workers_id = []
    
        for log in logs:
            id, time = log
            interval = time-min_value
            if interval > max_work:
                max_work = interval
            min_value = time
        
        min_value = 0
        for log in logs:
            id, time = log
            interval = time-min_value
            if interval == max_work:
                workers_id.append(id)
            min_value = time
        return min(workers_id)
