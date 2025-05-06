"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_list = []

        i, idx = 0, 0

        while i < len(s):

            if s[i] == " ":
                i += 1

            else:
                tmpStr = ""

                while s[i] != " ":
                    tmpStr += s[i]   
                    i += 1
                    if i == len(s):
                        break 

                new_list.append(tmpStr)
                idx += 1
        
        s = ""

        for i in range(len(new_list)-1, 0, -1):
            s += new_list[i] + " "
        s += new_list[0]

        return s