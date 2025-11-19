class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        The key idea is 
        - we need two pointer to solve this 
        - lets have a hashset for vowel lookup
        - traverse one point from start and one from end if vowel is present then switch it 
        - or may be wait until both the pointer find an vowel
        Key point : we cannot swap a str we need to convert the input to list
        TIme , space = o(n), o(n)
        look at the commented sol 
        """
        vowels = {"a", "e", "i", "o", "u"}
        s_lst = list(s)
        
        i, j = 0, len(s_lst) - 1
        
        while i < j:
            left = s_lst[i].lower()
            right = s_lst[j].lower()
            
            # move left pointer
            if left not in vowels:
                i += 1
                continue
            
            # move right pointer
            if right not in vowels:
                j -= 1
                continue
            
            # both are vowels → swap
            s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
            i += 1
            j -= 1
        
        return "".join(s_lst)
        




        # my code is slightly faster hands down congrooo brooo .

        # my code worked but chatgpt says the flow might be confusinf fix it the above is the fix
        # vowels = {"a","e","i","o","u"}
        # s_lst = list(s)
        # i = 0
        # j = len(s_lst) - 1
        # while i < j:# master mind i am moving both the pointer in single iteration which is a bit efficent just make sure to called .lower once as above code
        #     if s_lst[i].lower() not in vowels:
        #         i += 1
        #     if s_lst[j].lower() not in vowels:
        #         j -= 1
        #     if s_lst[i].lower() in vowels and s_lst[j].lower() in vowels:
        #         s_lst[i],s_lst[j] = s_lst[j],s_lst[i]
        #         i += 1
        #         j -= 1
        # return "".join(s_lst)
        