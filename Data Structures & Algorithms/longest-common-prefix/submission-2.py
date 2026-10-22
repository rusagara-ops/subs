class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for i in range(len(word)):
            for strng in strs:
                if i == len(strng) or strng[i] != word[i]:
                    return word[:i]

        return word