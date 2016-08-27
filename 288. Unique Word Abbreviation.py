__author__ = 'liuxiyun'
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.word_dic = {}
        for word in dictionary:
            key = self.getKey(word)
            if key in self.word_dic and self.word_dic[key]!=word:
                self.word_dic[key] = ""
            else:
                self.word_dic[key] = word


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = self.getKey(word)
        if key in self.word_dic:
            return self.word_dic[key] == word
        return True

    def getKey(self,word):
        return word if len(word)<2 else word[0]+str(len(word)-2)+word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
vwa = ValidWordAbbr(["d"])
print vwa.isUnique("dog")
print vwa.isUnique("dig")

