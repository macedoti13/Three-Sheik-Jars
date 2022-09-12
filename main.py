from tree import Tree
from node import Node
from jar import Jar


def checks_possible(jar1: Jar, jar2: Jar, jar3: Jar) -> bool:
    """_summary_

    Args:
        jar1 (Jar): _description_
        jar2 (Jar): _description_
        jar3 (Jar): _description_

    Returns:
        bool: _description_
    """    
    total_amount = jar1.current_amount + jar2.current_amount + jar3.current_amount
    total_capacity = jar1.capacity + jar2.capacity + jar3.capacity
    total_desired = jar1.desired_amount + jar2.desired_amount + jar3.desired_amount

    if total_amount != total_desired or total_capacity < total_desired:
        return False

    return True


def main():
    jar1 = Jar(16, 9, 0)
    jar2 = Jar(28, 11, 25)
    jar3 = Jar(29, 11, 6)
    tree = Tree()
    if checks_possible(jar1, jar2, jar3):
        tree.add(jar1, jar2, jar3)
        if tree.check_solution(tree.root):
            print(tree.level(tree.root))
        else:
            pass
        print(f'Amount of nodes is the tree: {tree.count}')
    else:
        print('No possible solution!')


if __name__ == "__main__":
    main()
