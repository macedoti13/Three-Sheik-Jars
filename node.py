from jar import Jar


class Node():


    def __init__(self, jar1: Jar, jar2: Jar, jar3: Jar) -> None:
        """Initializes the node object with three jars"""
        self.jar1 = jar1
        self.jar2 = jar2
        self.jar3 = jar3
        self.children = []
        self.parent = None


    def add_child(self, n) -> None:
        """Adds a child to a node

        Args:
            n (Node): child that will be added to the node
        """        
        self.children.append(n)
        n.parent = self


    def copy(self):    
        """Creates a copy of node

        Returns:
            Node: Identical copy of the node
        """        
        jars = [self.jar1, self.jar2, self.jar3]
        new_jars = []
        for jar in jars:
            new_jar = Jar(jar.capacity, jar.current_amount, jar.desired_amount)
            new_jars.append(new_jar)

        return Node(new_jars[0], new_jars[1], new_jars[2])


    def create_copies(self) -> list:    
        """Creates 6 identical copies of a node

        Returns:
            list: list of identical nodes
        """         
        nodes = []

        for _ in range(6):
            n = self.copy()
            nodes.append(n)

        return nodes


    def combinations(self) -> list:
        """All the combinations of jars that a node can have

        Returns:
            list: list of combinations
        """        
        combinations = [
            (self.jar1, self.jar2),
            (self.jar1, self.jar3),
            (self.jar2, self.jar1),
            (self.jar2, self.jar3),
            (self.jar3, self.jar1),
            (self.jar3, self.jar2)
        ]

        return combinations


    def state(self):
        """Current amount of water in each jar for a node

        Returns:
            tuple: tuple with the 3 amount of water for the three nodes
        """        
        return tuple([self.jar1.current_amount, self.jar2.current_amount, self.jar3.current_amount])

    
    def water_dump(self, jar_gives: Jar, jar_receives: Jar) -> None:
        """Performs water dump between two jars for a given node

        Args:
            jar_gives (Jar): jar that gives water
            jar_receives (Jar): jar that receives water
        """        
        jar_gives, jar_receives = Jar.water_dump(jar_gives, jar_receives)

    def check_water_dump_possibility(self, jar_gives, jar_receives):
        """Check if it's possible to perform a water dump between two jars for a given node

        Args:
            jar_gives (Jar): jar that gives water
            jar_receives (Jar): jar that receives water

        Returns:
            bool: true if it's possible to perform water dump
        """        
        return Jar.check_water_dump_possibility(jar_gives, jar_receives)


def check_solution(node: Node):
    """Function to check if the node has reached the solution, that is, for all nodes, 
       the current amount of water is equal to the desired amount of water

    Args:
        node (Node): node that will be tested

    Returns:
        bool: if the node is the solution
    """    
    jar1_done = node.jar1.current_amount == node.jar1.desired_amount
    jar2_done = node.jar2.current_amount == node.jar2.desired_amount
    jar3_done = node.jar3.current_amount == node.jar3.desired_amount

    return jar1_done and jar2_done and jar3_done
