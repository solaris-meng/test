
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        #print(s)
        i = j = 0
        i_s = j_s = s[0]
        cur = 0
        r = 0
        while i < len(s):
            #print('loop ')
            j = i
            cur_s = ''
            cur_l = 0
            while j < len(s):
                #print('i: %d, j:%d, cur_s:%s, sj:%s' % (i, j, cur_s, s[j]))
                if s[j] in cur_s:
                    m = j - i
                    #print('max:%s' % s[i:j])
                    r = m if m > r else r
                    break
                if i == j:
                    cur_s = s[i]
                    cur_l = 1
                else:
                    cur_s = s[i:j+1]
                    cur_l = len(cur_s)
                #print(cur_s)
                r = cur_l if cur_l > r else r
                j += 1
            i += 1
        return r


s = Solution()
#r = s.lengthOfLongestSubstring('p')
#r = s.lengthOfLongestSubstring('abcabcbb')
#r = s.lengthOfLongestSubstring('pwwkew')
r = s.lengthOfLongestSubstring('dvdf')
print(r)
