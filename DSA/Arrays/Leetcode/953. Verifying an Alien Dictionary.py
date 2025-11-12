class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        -Create a dict to hold the order of alien dict and its index val
        -comapre adjacent words in the list 
        - have a while loop to traverse till the end of letters where both words have diff val so we can check if they are sorted in lexigraphical order
        - if len of word 2 is less than word 1 instantly return False as its not sorted 
        - and after all this checks check if len of both words are less and comapre the dict index but we check the len because what if the both words lens are eq ?? and what if len of w1 is less than w2 if we directly do dict comapre it will give us index out of range errror so we check ( in both this cases we should return true)
        Time and space 
        - time = o(no of words * no char char)
        - space = o(len(order))
        """
        a_dict = {val:i for i,val in enumerate(order)}
        
        for i in range(1,len(words)):
            w1,w2 = words[i-1],words[i]
            j = 0
            while j < len(w1) and j < len(w2) and w1[j]  ==  w2[j]:
                j += 1
            
            if j == len(w2) and len(w1) > len(w2):
                return False
            
            if j < len(w1) and j < len(w2):
                if a_dict[w1[j]] > a_dict[w2[j]]:
                    return False
        return True
        