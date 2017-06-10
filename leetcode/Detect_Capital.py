# encoding: utf-8

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if 65 <= ord(word[0]) <= 90:
            capcount = 0
            for x in word[1:]:
                if 65 <= ord(x) <= 90:
                    capcount += 1
            if capcount == len(word[1:]):
                return True
            else:
                return False
        else:
            for x in word[1:]:
                if 65 <= ord(x) <= 90:
                    return False
            return True