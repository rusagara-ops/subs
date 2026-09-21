class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list)
        records = []
        patterns = defaultdict(int)

        # gonna have records = [(1,bob,home),...]

        for i in range(len(username)):
            records.append((timestamp[i],username[i],website[i]))
        
        records.sort()

        for record in records:
            visits[record[1]].append(record[2])

        for value in visits.values():
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    for k in range(j+1, len(value)):
                        pattern = (value[i],value[j],value[k])
                        patterns[pattern] += 1

        return list(max(patterns, key=patterns.get))




        

        
        