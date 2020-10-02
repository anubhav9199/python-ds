class LPS(object):
    
    def manacher_algo_lps(self,s,n):
        """
        PARAMETER
        --------------
        s = string
        n = string_len (int)

        manacher Algorithm is the fastest technique to find the longest pallindrome substring in any given string.

        RETURN
        ---------------
        Longest Pallindrome String(String)
        """
        # variables to use
        p = [0] * n
        c = 0
        r = 0
        maxlen = 0

        # Main Algorithm
        for i in range(n):
            mirror = 2*c-i # Finding the Mirror(i.e. Pivort to break) of the string
            if i < r:
                p[i] = (r - i) if (r - i) < p[mirror] else p[mirror]
            a = i + (1 + p[i])
            b = i - (1 + p[i])

            # Attempt to expand palindrome centered at currentRightPosition i 
            # Here for odd positions, we compare characters and 
            # if match then increment LPS Length by ONE 
            # If even position, we just increment LPS by ONE without 
            # any character comparison
            while a<n and b>=0 and s[a] == s[b]:
                p[i] += 1
                a += 1
                b -= 1
            if (i + p[i]) > r:
                c = i
                r = i + p[i]
                if p[i] > maxlen:               # Track maxLPSLength
                    maxlen = p[i]
        i = p.index(maxlen)
        return s[i-maxlen:maxlen+i][1::2]

    def longest_pallindrome(self, s: str) -> str:
        s = '#'.join(s)
        s = '#'+s+'#'

        # Calling Manacher Algorithm
        return self.manacher_algo_lps(s,len(s))

def main():

    # Input to enter
    input_string = "abbbacdcaacdca"

    # Initialising object
    lps = LPS()

    # Calling the longest pallindrome algorithm
    s = lps.longest_pallindrome(input_string)
    print("LPS Using Manacher Algorithm {}".format(s))

# Calling Main Function
if __name__ == "__main__":

    main()