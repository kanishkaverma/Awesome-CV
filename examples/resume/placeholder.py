import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_pointer, b_pointer = 0, 0
        disc = {}
        max_len = -math.inf
        while b_pointer < len(s):
            if s[b_pointer] not in disc:
                disc[s[b_pointer]] = b_pointer
                b_pointer += 1
            else:
                disc[s[b_pointer]] = disc[s[b_pointer]] + 1
                a_pointer = disc[s[b_pointer]]
                b_pointer += 1

            max_len = max(max_len, b_pointer - a_pointer + 1)
        return max_len


# pwwkew
