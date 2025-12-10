class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0 
        write = 0 
        n = len(chars)

        while read < n:
            current = chars[read]
            count = 0

            #increase the read and count until next char is found
            while read < n and chars[read] == current:
                read += 1
                count += 1
            
            #one next char is found break the above while loop 
            chars[write] = current
            write += 1

            #if count > 1 then deal with it 
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write+= 1
        return write