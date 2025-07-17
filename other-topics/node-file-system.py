from collections import defaultdict


class Node:
    def __init__(self, is_directory=False):
        self.is_directory = is_directory
        self.content = ''
        self.children = defaultdict(Node)

class FileSystem:
    def __init__(self):
        self.root = Node(is_directory=True)

    def _find_node(self, path): #, create=False):
        parts = path.split('/')
        current = self.root
        for part in parts:
            if not part:
                continue
            if part not in current.children:
                return None
            current = current.children.get(part)
        return current
        # for part in parts:
        #     if not part:
        #         continue
        #     current = current.children.get(part)
        #     if create:
        #         current[part] = {}
        #     if current is None:
        #         return None
        # return current

    def mkdir(self, path):
        parts = path.split('/')
        current = self.root
        for part in parts:
            if not part:
                continue
            current = current.children[part]
        current.is_directory = True

    def get_size(self, path):
        node = self._find_node(path)
        if node is None:
            return -1
        return self._check_size(node)

    def _check_size(self, node):
        if not node.is_directory:
            return len(node.content)
        total_size = 0
        for child_node in node.children.values():
            total_size += self._check_size((child_node))
        return total_size

    def ls(self, path: str):
        node = self._find_node(path)
        if node is None:
            return "Error: Path not found"
        if not node.is_directory:
            return path.split('/')[-1]
        # if isinstance(node, str):
        return node.children.keys()

    def add_content_to_file(self, path: str, content: str):
        parts = path.split('/')
        filename = parts.pop()
        curr = self.root
        for part in parts:
            if not part:
                continue
            curr = curr.children[part]
        filenode = curr.children[filename]
        filenode.is_directory = False
        filenode.content += content

    def read_content_from_file(self, path):
        node = self._find_node(path)
        if node is None or node.is_directory:
            return "Error; Not a file or path not found."
        return node.content

if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir(path='/Users/j0c0p72/Downloads/hello/work')
    fs.add_content_to_file(path='/Users/j0c0p72/Downloads/hello/work/file.txt', content='hello, Jae')
    # def readFile(fs, path):
    #     parts = path.split('/')
    #     current = fs.root
    #     for part in parts:
    #         if not part:
    #             continue
    #         if part not in current.children:
    #             return "Error: Path not found"
    #         current = current.children[part]
    #     return current.content
    #
    # print(readFile(fs, '/Users/j0c0p72/Downloads/hello/work/file.txt'))
    print(fs.read_content_from_file('/Users/j0c0p72/Downloads/hello/work/file.txt'))
    print(fs.ls(path = '/Users/j0c0p72/Downloads/hello/work'))


