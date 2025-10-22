class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        This can be done by string slicing 
        time = o(n)
        space = o(1)
        """
        count = 0
        for detail in details:
            #added all the things for any follow question in interview all we need here is just age
            phone_num = detail[:10] #start is inclusive and stop is exclusive # the first ten char for phn num
            gender = detail[10:11] # only include one char 10 which is gender
            age = detail[11:13] #index  11 and 12 are age 
            seat_allocated = detail[13:]

            #put the check cond 
            if int(age) > 60:
                count += 1
        return count

        