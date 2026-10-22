class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for i in range(len(word)):
            for strng in strs:
                if word[i] not in strng:
                    return word[:i]
                else:
                    continue

        return word