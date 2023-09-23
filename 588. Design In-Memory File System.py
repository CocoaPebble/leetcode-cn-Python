from typing import List
import collections

class FileSystem:

    def __init__(self):
        self.root = {}


    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.root.keys())
        path = path.split('/')
        node = self.root
        for p in path[1:]:
            if p not in node:
                return []
            node = node[p]
        if isinstance(node, str):
            return [path[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        path = path.split('/')
        node = self.root
        for p in path[1:]:
            if p not in node:
                node[p] = {}
            node = node[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')
        node = self.root
        for p in path[1:-1]:
            if p not in node:
                node[p] = {}
            node = node[p]
        if path[-1] not in node:
            node[path[-1]] = content
        else:
            node[path[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split('/')
        node = self.root
        for p in path[1:]:
            node = node[p]
        return node


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)