class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split(" ")
        if len(pattern) != len(list_s):
            return False
        seen_word = set()
        s_pattern_map = {}
        for idx, chr in enumerate(pattern):
            print(idx, list_s[idx])
            if chr in s_pattern_map.keys():
                if s_pattern_map[chr] != list_s[idx]:
                    return False
            elif list_s[idx] in seen_word:
                return False
            
            seen_word.add(list_s[idx])
            s_pattern_map[chr] = list_s[idx]
            
        
        return True
