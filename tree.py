from jar import Jar
from node import Node, check_solution

class Tree():    


    def __init__(self) -> None:

        self.root = None
        self.count = 0
        self.states = []


    def add(self, n: Node, parent: Node = None) -> None:
        if n.state not in self.states:
            if self.root == None and parent == None:
                self.root = n
            else:
                parent.add_child(n)

            self.states.append(n.state())
            self.count += 1 


    def remove(self, n: Node) -> None:
        if n == self.root:
            self.root = None
        else:
            n.parent = None
            n.children.clear()

        self.count -= 1
        self.states.remove(n.state)
        del n


    def level(self, n: Node) -> int:    
        i = 0

        while n != self.root:
            n = n.parent
            i += 1

        return i


    def _build_tree_for(self, n: Node) -> None:
        
        i = 0
        for node in n.create_copies():
            combination = node.combinations()[i]
            if node.check_water_dump_possibility(combination[0], combination[1]):
                node.water_dump(combination[0], combination[1])
                if node.state() not in self.states:
                    self.add(node, parent=n)
                else:
                    del node
            else:
                del node
            i+=1


    def _build_solutions_tree(self, node_list: list):
        next_nodes = []
        for node in node_list:
            if check_solution(node) == True:
                return self.level(node)
        for node in node_list:
            self._build_tree_for(node)
            for child in node.children:
                next_nodes.append(child)
        return self._build_solutions_tree(next_nodes)



    def build_tree(self):
        return self._build_solutions_tree([self.root])