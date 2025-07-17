from collections import defaultdict
from typing import List

class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if isinstance(node, str):
            return [path.split('/')[-1]]
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        node = self._traverse(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split('/')
        curr = self.root
        for part in parts[1:-1]:
            if part not in curr:
                curr[part] = {}
            curr = curr[part]
        if parts[-1] not in curr:
            curr[parts[-1]] = ''
        curr[parts[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        # key = filePath.split('/')[-1]
        # node = self._traverse(filePath)
        # return node[key]
        parts = filePath.split('/')
        curr = self.root
        for part in parts[1:-1]:
            curr = curr[part]
        return curr[parts[-1]]

    def _traverse(self, path: str, create: bool = False):
        if path == '/':
            return self.root
        parts = path.split('/')
        curr = self.root
        for part in parts[1:]:
            if part not in curr:
                if create:
                    curr[part] = {}
                else:
                    return None
            curr = curr[part]
        return curr

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
if __name__ == "__main__":
    obj = FileSystem()
    path = "/Users/j0c0p72/Downloads/hello/work"
    print(obj.mkdir(path))
    filePath = path.rstrip('/') + "/myfile.txt"
    obj.addContentToFile(filePath, "Hyunni")
    content = obj.readContentFromFile(filePath)
    print(content)
    listing = obj.ls(path)
    print("Listing:", listing)