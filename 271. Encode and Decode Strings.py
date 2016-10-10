__author__ = 'liuxiyun'
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for string in strs:
            res += (str(len(string)) + '*' + string)
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res

# Your Codec object will be instantiated and called as such:
strs = ["ab","cde"]
codec = Codec()
print codec.decode(codec.encode(strs))