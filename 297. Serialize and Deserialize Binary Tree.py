__author__ = 'liuxiyun'
class Codec:
    def serialize(self, root):
        self.vals = []
        self.help_s(root) #['1','2','#','#','3','4'.....]
        return ' '.join(self.vals) # "1 2 # # 3 4 # # 5 # #"

    def help_s(self,node): # pre-order
        if node:
            self.vals.append(str(node.val))
            self.help_s(node.left)
            self.help_s(node.right)
        else:
            self.vals.append('#')

    def deserialize(self, data):
        self.vals2 = iter(data.split())
        return self.help_d()

    def help_d(self):
        val = next(self.vals2)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.help_d()
        node.right = self.help_d()
        return node