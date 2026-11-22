class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        if len(strs) == 0:
            return ""

        for string in strs:
            length = str(len(string))
            encoded += length + "#" + string
        return encoded


    def decode(self, s: str) -> List[str]:
        Output = []

        word = s

        #  10#HelloJames
        while len(word) != 0:
            hash_loc = word.find("#")
            length = int(word[:hash_loc])
            Output.append(word[hash_loc+1:hash_loc+1+length])
            word = word[hash_loc + 1 + length:]
        return Output
            
        
