class Solution:
    def longestPalindrome(self, s):
        start = 0
        longest_pal_count = 0
        longest_pal = ''
        i = 0
        const_i = 0
        while start < len(s):
            for j in range(len(s)):
                i += const_i
                i += j
                if s[start:(i+1)] == s[i:None:-1] or s[start:(i+1)] == s[i-len(s):(start-1):-1]:
                    if len(s[start:(i+1)]) > longest_pal_count:
                        longest_pal = s[start:(i+1)]
                        longest_pal_count = len(s[start:(i+1)])
                        i = 0
                else:
                    i = 0
            start += 1
            const_i += 1
        return(longest_pal)
