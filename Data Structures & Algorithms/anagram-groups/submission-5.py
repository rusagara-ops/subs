class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        result = []

        for word in strs:
            newword = ''.join(sorted(word))
            hashmap[newword].append(word)

        for value in hashmap.values():
            result.append(value)

        return result
                
