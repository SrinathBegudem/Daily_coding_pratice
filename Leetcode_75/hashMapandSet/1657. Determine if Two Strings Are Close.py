from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        

        def optimal_clean_sol():
            """
            We use libraries and packages here, looks clean and efficent.
            """

            #condition 1 : if len of word1 and word2 are diff return false
            if len(word1) != len(word2):
                return False
            
            #condition 2: check if they have same char in both the words 
            counts1 = Counter(word1)
            counts2 = Counter(word2)

            if counts1.keys() != counts2.keys():
                return False
            
            # check if freq can be interchanged by sorting
            return sorted(counts1.values()) == sorted(counts2.values())

        def normal_sol():
            """
            Here we dont use any libraries or packages
            """

            #case 1 : if len of words are not equal return false
            if len(word1) != len(word2): return False

            #case 2: check if both words have same char or not, if not the operation 2 is not possible 
            freq1 = dict()
            for char in word1:
                freq1[char] = freq1.get(char,0) + 1

            freq2 = dict()
            for char in word2:
                freq2[char] = freq2.get(char,0) + 1
            
            #mannually checking if keys are same or not 
            # if len of dicts is diff then differnt keys return False immediately 
            if len(freq1) != len(freq2): return False

            for key in freq1:
                # if the key is not in freq2 then they have diff keys
                if key not in freq2:
                    return False

            #case 3: check if we can manupliate freq and make the both words eq, the simple trick is to sort and check if freq match if they dont then no matter what we cannot attain word 1 from word2 or viceversa
            counts1 = sorted(freq1.values())
            counts2 = sorted(freq2.values())
            for i in range(len(counts1)):
                if counts1[i] != counts2[i]: return False
            return True

        return normal_sol()
