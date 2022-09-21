from node import Node, check_solution

class Tree():    


    def __init__(self) -> None:
        """Initializes tree object"""
        self.root = None
        self.count = 0
        self.states = []


    def add(self, n: Node, parent: Node = None) -> None:
        """Adds node to the tree

        Args:
            n (Node): node that will be added
            parent (Node, optional): parent of the node. Defaults to None.
        """        
        if n.state not in self.states:
            if self.root == None and parent == None:
                self.root = n
            else:
                parent.add_child(n)

            self.states.append(n.state())
            self.count += 1 


    def remove(self, n: Node) -> None:
        """Removes a given node from the tree

        Args:
            n (Node): node that will be removed and deleted
        """        
        if n == self.root:
            self.root = None
        else:
            n.parent = None
            n.children.clear()

        self.count -= 1
        self.states.remove(n.state)
        del n


    def level(self, n: Node) -> int:   
        """Level of a given node of the tree

        Args:
            n (Node): node that we wan't to know the level

        Returns:
            int: the level of the node
        """         
        i = 0

        while n != self.root:
            n = n.parent
            i += 1

        return i


    def _build_tree_for(self, n: Node) -> None:
        """Builds the sucession tree for a given node

        Args:
            n (Node): node that we wan't the sucession tree for
        """        
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
        """Builds the solution tree for a list of nodes

        Args:
            node_list (list): list of nodes that the tree will be built for

        Returns:
            bool: if it has reached a solution node
        """
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
        """Finds the solution for a tree

        Returns:
            int: Amount of movements necessary to reach the solution
        """        
        return self._build_solutions_tree([self.root])