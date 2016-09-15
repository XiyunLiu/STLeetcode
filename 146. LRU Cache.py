__author__ = 'liuxiyun'
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.stack = []
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dic[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.dic:
            if len(self.stack) == self.capacity:
                needRemove = self.stack.pop(0)
                self.dic.pop(needRemove)
        else:
            self.stack.remove(key)

        self.dic[key] = value
        self.stack.append(key)

