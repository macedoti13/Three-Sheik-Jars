from jar import Jar


class Node():


    def __init__(self, jar1: Jar, jar2: Jar, jar3: Jar, children: list = [], parent = None) -> None:
        """_summary_

        Args:
            jar1 (Jar): _description_
            jar2 (Jar): _description_
            jar3 (Jar): _description_
            children (list, optional): _description_. Defaults to [].
            parent (_type_, optional): _description_. Defaults to None.
        """        
        self.jar1 = jar1
        self.jar2 = jar2
        self.jar3 = jar3
        self.children = children
        self.parent = parent


    def add_child(self, n):
        """_summary_

        Args:
            n (_type_): _description_
        """        
        self.children.append(n)
        n.parent = self


    def copy(self):
        """_summary_

        Returns:
            _type_: _description_
        """                
        jars = [self.jar1, self.jar2, self.jar3]
        new_jars = []
        for jar in jars:
            new_jar = Jar(jar.capacity, jar.current_amount, jar.desired_amount)
            new_jars.append(new_jar)

        return Node(new_jars[0], new_jars[1], new_jars[2])


    def combinations(self) -> list:
        """_summary_

        Returns:
            list: _description_
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


    def check_water_dump_possible(self, jar_gives: Jar, jar_receives: Jar) -> bool:
        """_summary_

        Args:
            jar_gives (Jar): _description_
            jar_receives (Jar): _description_

        Returns:
            bool: _description_
        """        
        return Jar.check_water_dump_possibility(jar_gives, jar_receives)


    def water_dump(self, jar_gives: Jar, jar_receives: Jar) -> None:
        """_summary_

        Args:
            jar_gives (Jar): _description_
            jar_receives (Jar): _description_
        """        
        jar_gives, jar_receives = Jar.water_dump(jar_gives, jar_receives)


    def check_water_dump_possibility(self, jar_gives, jar_receives):
        """_summary_

        Args:
            jar_gives (_type_): _description_
            jar_receives (_type_): _description_

        Returns:
            _type_: _description_
        """        
        return Jar.check_water_dump_possibility(jar_gives, jar_receives)


    def state(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        return tuple([self.jar1.current_amount, self.jar2.current_amount, self.jar3.current_amount])
    

    def check_solution(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """        
        jar1_done = self.jar1.current_amount == self.jar1.desired_amount
        jar2_done = self.jar2.current_amount == self.jar2.desired_amount
        jar3_done = self.jar3.current_amount == self.jar3.desired_amount

        return jar1_done and jar2_done and jar3_done
    

    def create_copies(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """        
        nodes = []

        for _ in range(6):
            n = self.copy()
            nodes.append(n)

        return nodes
    