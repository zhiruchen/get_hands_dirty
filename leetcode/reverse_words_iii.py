# encoding: utf-8

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ss = s.split()
        
        def rev(word):
            words = list(word)
            wl = len(words)
            i, j = 0, wl-1
            while i < wl/2:
                words[i], words[j] = words[j], words[i]
                i, j = i+1, j-1
            return ''.join(words)

        return ' '.join(map(rev, ss))

if __name__ == '__main__':
    s = Solution()
    print s.reverseWords("Let's take LeetCode contest")