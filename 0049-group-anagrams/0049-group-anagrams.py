class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i in strs:
            word = "".join(sorted(i))
            if word not in my_dict:
                my_dict[word] = [i]
            else:
               my_dict[word].append(i)

        return list(my_dict.values())