from jar import Jar


class Node():


    def __init__(self, jar1: Jar, jar2: Jar, jar3: Jar) -> None:
        self.jar1 = jar1
        self.jar2 = jar2
        self.jar3 = jar3
        self.children = []
        self.parent = None


    def add_child(self, n) -> None:
        self.children.append(n)
        n.parent = self


    def copy(self):    
        jars = [self.jar1, self.jar2, self.jar3]
        new_jars = []
        for jar in jars:
            new_jar = Jar(jar.capacity, jar.current_amount, jar.desired_amount)
            new_jars.append(new_jar)

        return Node(new_jars[0], new_jars[1], new_jars[2])


    def create_copies(self) -> list:     
        nodes = []

        for _ in range(6):
            n = self.copy()
            nodes.append(n)

        return nodes


    def combinations(self) -> list:
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
        return tuple([self.jar1.current_amount, self.jar2.current_amount, self.jar3.current_amount])

    
    def water_dump(self, jar_gives: Jar, jar_receives: Jar) -> None:
        jar_gives, jar_receives = Jar.water_dump(jar_gives, jar_receives)

    def check_water_dump_possibility(self, jar_gives, jar_receives):
        return Jar.check_water_dump_possibility(jar_gives, jar_receives)


def check_solution(node: Node):
    jar1_done = node.jar1.current_amount == node.jar1.desired_amount
    jar2_done = node.jar2.current_amount == node.jar2.desired_amount
    jar3_done = node.jar3.current_amount == node.jar3.desired_amount

    return jar1_done and jar2_done and jar3_done
