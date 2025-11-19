class Solution:
    def reverseWords(self, s: str) -> str:
        """
        The key idea
        - As string is immutable, its better to store/ work with list and join at the end 
        - So creating list and working with it aviods mutiple creation of new str when we change something (which is not very efficentive)
        - we split by white spaces " " and store in list
        - we do another preprocessing step to clear out the white spaces 
        - and reverse the list and join. 

        Imp points
        - whenever we split on white spaces python gives whats there in btw them when it sees what space so if you have only white space the it will return empty string
        - So every time Python sees " ", it cuts, and whatever is between cuts becomes a list item.
        "  hello   world  "
        ^ ^     ^   ^ ^  
        | |     |   | |
        "" "" "hello" "" "" "world" "" ""
        ["", "", "hello", "", "", "world", "", ""]
        Something like above 
        - we can also use  if s_list[i].isalnum for this sum it works but there might be a follow up questioon where hypens commos might be included so empt str check works perfectly
        time = o(n) , space = o(n)
        """

        s_list = s.split(" ") #split the str with white spaces and words 
        res = [] # to hold the processed strings
        # one pass: we remove spaces and to reverse traversal in single pass ( traversal from right to left)
        n = len(s_list) - 1
        for i in range(n,-1,-1):
            if s_list[i] == "": # or if not s_list[i]: continue
                continue 
            res.append(s_list[i])
        return " ".join(res)

        