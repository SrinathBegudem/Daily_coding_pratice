class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def pythonic_sol():
            """
            This is just pythonic way of writing things neatly but same time and space complexity
            """
            seen = set()
            for e in emails:
                # divided into local and domain
                local,domain = e.split("@")
                #in local split when there is + and that the first indx in that if any dot remove 
                local = local.split("+")[0].replace(".","")
                seen.add(local+"@"+domain)
            return len(seen)
        return pythonic_sol()







        def verbose_sol():
            """
            Key points 
            - dot in the local name should be ignored 
            - char after the + symbol should be ignored
            - both the above rules will not be applicable to the domain names
            My intuition here is that 
            - we do preprocessing to align with rules 
            - and have a set to check if the pre process list already seen
            time and space 
            Time = o(m*n)
            space = o(max(o(m*n))
            """
            seen = set() # to store the unquie email addresses #o(m)

            #lets loop to each email and preprocess it 
            for email in emails: # o(n)
                temp = list() # because i think instead of doing str concat (which create a new obj after every concat), its better to use list #O(t)
                # unprocessed = email.spilt("@")
                i = 0 
                while email[i] != "@": #o(m)
                    if email[i] == "+":
                        i += 1
                        while email[i] != "@":
                            i += 1
                            continue
                        break
                    elif email[i] == ".":
                        i += 1
                        continue 
                    else:
                        temp.append(email[i])
                        i += 1
                #once the loop breaks we skip all the char after + and skip dots 
                # and now i is at @ we add the domain as is 
                temp.append(email[i:])
                processed_s  =  "".join(temp)
                print(processed_s)
                seen.add(processed_s)
            return len(seen)                