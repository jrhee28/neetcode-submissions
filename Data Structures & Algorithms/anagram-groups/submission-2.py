class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            sort_str = "".join(sorted(string))
            if sort_str not in groups:
                groups[sort_str] = []
            groups[sort_str].append(string)
        return list((groups.values()))
            
                
        