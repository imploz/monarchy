

class BatchRegistry:
    def __init__(self, monarchs):
        self.monarchs = monarchs

    def __iter__(self):
        return iter(self.monarchs)





