from jar import Jar
from node import Node

class Tree():    


    def __init__(self, root: Node = None, count: int = 0, states: list = []) -> None:

        self.root = root
        self.count = count
        self.states = states


    def add(self, jar1: Jar, jar2: Jar, jar3: Jar, parent: Node = None) -> None:
        """_summary_

        Args:
            jar1 (Jar): _description_
            jar2 (Jar): _description_
            jar3 (Jar): _description_
            parent (Node, optional): _description_. Defaults to None.
        """        
        n = Node(jar1, jar2, jar3)

        if n.state() not in self.states:
            if parent == None and self.root == None:
                self.root = n 
            elif parent != None:
                n.parent = parent
                parent.add_child(n)

            self.states.append(n.state())
            self.count += 1


    def remove(self, n: Node) -> None:
        """_summary_

        Args:
            n (Node): _description_
        """        
        if n == self.root:
            self.root = None
        else:
            n.parent = None
            n.children.clear()

        self.count -= 1
        self.states.remove(n.state())
        del n


    def level(self, n: Node) -> int:
        """_summary_

        Args:
            n (Node): _description_

        Returns:
            int: _description_
        """        
        i = 0

        while n != self.root:
            n = n.parent
            i += 1

        return i


    def check_solution(self, n: Node) -> bool:
        """_summary_

        Args:
            n (Node): _description_

        Returns:
            bool: _description_
        """        
        return n.jar1.current_amount == n.jar1.desired_amount and n.jar2.current_amount == n.jar2.desired_amount and n.jar3.current_amount == n.jar3.desired_amount