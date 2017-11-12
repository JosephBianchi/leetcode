# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         big = []
#         current = []
#         for j in range(len(s)):
#             if s[j] not in big:
#                 big.append(s[j])
#             else:
#                 for j in range(len(big), len(s)):
#                     if s[j] not in current:
#                         current.append(s[j])
#                 if len(current) > len(big):
#                     big = current
#                 return len(big)
#
# print(Solution().lengthOfLongestSubstring("hello"))


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar: and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

    def test(self, name, actual, expected):
        if actual == expected:
            print(".....GREEN")
            print("name: ", name)
            print("actual: ", actual)
            print("expected", expected)
        else:
            print("RED..........")
            print("name: ", name)
            print("actual: ", actual)
            print("expected", expected)
actual = Solution().lengthOfLongestSubstring("abcabccabcd")
Solution().test("sub_string", actual, 4)
