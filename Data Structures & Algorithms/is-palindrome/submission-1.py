class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        word = ""
        for letter in s:
            if letter.isalnum():
                word += letter
        word = word.lower()

        if len(word) <= 1:
            return True

        first = word[:len(word)//2]
        if len(word)%2 == 0:
            second = word[len(word)//2:]
        else:
            second = word[len(word)//2 + 1:]
        second = second[::-1]
        print(second)
        if second == first:
            return True
        
        return False
        
        
