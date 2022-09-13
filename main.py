from jar import Jar
from tree import Tree
from node import Node


def checks_possible(jar1: Jar, jar2: Jar, jar3: Jar) -> bool:
    """Checks if there's a solution for a specific jar organization

    Args:
        jar1 (Jar): first jar 
        jar2 (Jar): second jar
        jar3 (Jar): third jar

    Returns:
        bool: True if there's a solution for the problem
    """    
    total_amount = jar1.current_amount + jar2.current_amount + jar3.current_amount
    total_capacity = jar1.capacity + jar2.capacity + jar3.capacity
    total_desired = jar1.desired_amount + jar2.desired_amount + jar3.desired_amount

    if total_amount != total_desired or total_capacity < total_desired:
        return False

    return True


def main():
    with open('saida_T1.txt', 'w') as s:
        with open('entrada_exemplo_T1.txt') as f:

            i = 0

            for line in f.readlines():

                if len(line.split()) > 1:
                    # writes line in output file
                    s.write(line)

                    # take the numbers of the line
                    numbers = line.split()

                    # tests what are the numbers representing
                    if i == 0:
                        capacities = [int(number) for number in numbers]
                        i += 1
                    elif i == 1: 
                        amounts = [int(number) for number in numbers]
                        i += 1
                    elif i == 2:
                        desires = [int(number) for number in numbers]
                        i += 1

                else:
                    # create jars
                    jar1 = Jar(capacities[0], amounts[0], desires[0])
                    jar2 = Jar(capacities[1], amounts[1], desires[1])
                    jar3 = Jar(capacities[2], amounts[2], desires[2])

                    # checks if it's possible
                    if checks_possible(jar1, jar2, jar3):
                        # create tree
                        tree = Tree()
                        tree.add( Node(jar1, jar2, jar3))

                        # get solution 
                        solution = tree.build_tree()
                    else:
                        solution = 'There\'s no solution!'

                    # write solution on output file
                    s.write(f'Movimentos: {solution}\n')

                    # restart i
                    i = 0

                    # restart lists
                    capacities.clear()
                    amounts.clear()
                    desires.clear()


if __name__ == "__main__":
    main()