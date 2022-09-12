from node import Node
from tree import Tree
from jar import Jar

jar1 = Jar(12, 10, 4)
jar2 = Jar(25, 20, 20)
jar3 = Jar(17, 11, 17)
tree = Tree()

tree.add(jar1, jar2, jar3)
print(tree.count)

n = Node(jar1, jar2, jar3)
tree.root.add_child(n)
tree.add_node(n)
print(tree.count)

print(tree.root)
print(tree.root.children[0])
print(tree.root.children[0].parent)