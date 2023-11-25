from typing import List, Any, Union
class DecisionTreeNode:
    def __init__(
        self,
        attribute: int,
        thresholds: List[Any],
        descendants: List[Union["DecisionTreeNode", bool]],
    ):
        self.attribute = attribute
        self.thresholds = thresholds
        self.descendants = descendants

    def evaluate(self, data: List[Any]) -> bool:
        value = data[self.attribute]
        for i in range(len(self.thresholds)):
            if value < self.thresholds[i]:
                if self.descendants[i] == True or self.descendants[i] == False:
                    return self.descendants[i]
                return self.descendants[i].evaluate(data)
        if self.descendants[-1] == True or self.descendants[-1] == False:
            return self.descendants[-1]
        return self.descendants[-1].evaluate(data)


class DecisionTree:
    def __init__(self, first_node):
        self.first_node = first_node

    def evaluate(self, data: List[Any]) -> bool:
        return self.first_node.evaluate(data)


data = [
    ([46.85, True, 0], True),
([46.70, True, 0], True),
([31.91, True, 0], False),
([1.86, False, 2], False),
([51.51, True, 0], True),
([9.94, True, 0], False),
([13.79, False, 2], False),
([45.60, True, 2], True),
([48.02, False, 0], True),
([11.74, False, 1], False),
([56.77, True, 1], True),
([8.68, True, 2], False),
([9.15, False, 1], False),
([24.31, True, 2], True),
([7.10, True, 0], False),
([38.88, True, 1], True),
([38.88, True, 0], False),
([49.58, False, 0], True),
([47.45, False, 1], True),
([27.19, True, 1], True),
([27.19, False, 1], False),
([25.75, False, 0], False),
([25.75, False, 2], True),
([24.09, False, 0], False),
([52.10, False, 0], True),
([15.87, True, 2], True),
([23.55, False, 2], True),
([35.86, True, 2], True)

]

# constants
LENGTH = 0
CHOSEN_BETTER = 1
FEEDERS = 2

# Tuto funkci implementuj.
def make_decision_tree() -> 'DecisionTree': 
    node3 = DecisionTreeNode(1, [True], [False, True]) #asi špatně
    node2 = DecisionTreeNode(2, [1,2,3], [False, node3, True]) #asi špatně
    node1 = DecisionTreeNode(0, [15],[False, node2])  
    node0 = DecisionTreeNode (0, [45],[node1, True])
   
    
    
    
    

    
    return DecisionTree(node0)


# Príklad stromu, ktorý kupi ovocie, ak ma karlik vela penazi, alebo doma ovocie nema
def make_example_tree() -> DecisionTree:
    # Uzol pozerá vlastnosť 2 - Karlíkove peniaze, hranicu má na hodnote 2, pod
    # ktorou vráti False, a na/nad ňou vráti True
    node1 = DecisionTreeNode(2, [2], [False, True])

    # Uzol pozerá vlastnosť 1 - či má Karlík doma ovocia, hranica je na hodnote
    # True, teda pre False, sa vráti True a pre True sa ide do node1
    node2 = DecisionTreeNode(1, [True], [True, node1])
    

    return DecisionTree(node2)


# tree = make_example_tree()
tree = make_decision_tree()

data_points = [
    ([46.85, True, 0], True),
([46.70, True, 0], True),
([31.91, True, 0], False),
([1.86, False, 2], False),
([51.51, True, 0], True),
([9.94, True, 0], False),
([13.79, False, 2], False),
([45.60, True, 2], True),
([48.02, False, 0], True),
([11.74, False, 1], False),
([56.77, True, 1], True),
([8.68, True, 2], False),
([9.15, False, 1], False),
([24.31, True, 2], True),
([7.10, True, 0], False),
([38.88, True, 1], True),
([38.88, True, 0], False),
([49.58, False, 0], True),
([47.45, False, 1], True),
([27.19, True, 1], True),
([27.19, False, 1], False),
([25.75, False, 0], False),
([25.75, False, 2], True),
([24.09, False, 0], False),
([52.10, False, 0], True),
([15.87, True, 2], True),
([23.55, False, 2], True),
([35.86, True, 2], True)

]

# Evaluate each data point
for data, label in data_points:
    prediction = tree.evaluate(data)
    print(f"Data: {data}")
    print(f"Predicted: {prediction}")
    print(f"Actual: {label}")
    print("------------------------")