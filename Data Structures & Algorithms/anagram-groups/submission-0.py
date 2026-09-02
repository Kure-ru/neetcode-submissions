class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagram_dict:
                anagram_dict[key] = []
            
            anagram_dict[key].append(word)

        return list(anagram_dict.values())