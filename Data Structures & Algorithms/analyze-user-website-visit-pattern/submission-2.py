class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        visits = defaultdict(list)
        records = []
        patterns = defaultdict(int)

        for i in range(len(username)):
            records.append((timestamp[i],username[i],website[i]))
        
        records.sort()

        for record in records:
            visits[record[1]].append(record[2])

        
        for value in visits.values():
            patternset = set()
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    for k in range(j+1, len(value)):
                        pattern = (value[i],value[j],value[k])
                        patternset.add(pattern)

            for pattern in patternset:
                patterns[pattern] += 1

        maximum = max(patterns.values())
        result = []

        for key,value in patterns.items():
            if value == maximum:
                result.append(key)
        result.sort()

        return list(result[0])





        

        
        