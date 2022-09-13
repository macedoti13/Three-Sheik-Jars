from jar import Jar
from tree import Tree
from node import Node

def checks_possible(jar1: Jar, jar2: Jar, jar3: Jar) -> bool:
    total_amount = jar1.current_amount + jar2.current_amount + jar3.current_amount
    total_capacity = jar1.capacity + jar2.capacity + jar3.capacity
    total_desired = jar1.desired_amount + jar2.desired_amount + jar3.desired_amount

    if total_amount != total_desired or total_capacity < total_desired:
        return False

    return True

def main():
    jar1 = Jar(14, 9, 5)
    jar2 = Jar(29, 23, 2)
    jar3 = Jar(25, 0, 25)
    
    if checks_possible(jar1, jar2, jar3):
        tree = Tree()
        tree.add(Node(jar1, jar2, jar3))
        solution = tree.build_tree()
        print('Amount of movements for solution:', solution)
    else:
        print('There\'s no solution!')

if __name__ == "__main__":
    main()