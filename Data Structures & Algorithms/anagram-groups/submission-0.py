class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for item in strs:
            s = sorted(item)
            x = "".join(s)
            if x not in dictionary:
                dictionary[x] = [item]
            else:
                dictionary[x].append(item)
        return list(dictionary.values())