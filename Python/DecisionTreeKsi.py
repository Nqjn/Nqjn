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
    ([10.99, True, 2], True),
    ([5.50, False, 2], True),
    ([5.50, False, 1], False),
    ([1.99, True, 0], True),
    ([4.50, False, 0], False),
    ([4.50, True, 1], True),
    ([0.99, True, 2], True),
    ([3.99, False, 1], True),
    ([3.99, True, 0], False),
    ([0.99, False, 0], True)
]

# constants
COST = 0
HAS_AT_HOME = 1
MONEY = 2

# Tuto funkci implementuj.
def make_decision_tree() -> 'DecisionTree':  
    
    node4 = DecisionTreeNode (0, [5], [True, False])
    node3 = DecisionTreeNode(2, [2],[True, False])
    node2 = DecisionTreeNode(2, [0, 2], [node4, True])
    node1 = DecisionTreeNode(1, [1], [node4, True])
    node0 = DecisionTreeNode(1, [True], [node1, node2])
    
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
    ([10.99, True, 2], True),
    ([5.50, False, 2], True),
    ([5.50, False, 1], False),
    ([1.99, True, 0], True),
    ([4.50, False, 0], False),
    ([4.50, True, 1], True),
    ([0.99, True, 2], True),
    ([3.99, False, 1], True),
    ([3.99, True, 0], False),
    ([0.99, False, 0], True)
]

# Evaluate each data point
for data, label in data_points:
    prediction = tree.evaluate(data)
    print(f"Data: {data}")
    print(f"Predicted: {prediction}")
    print(f"Actual: {label}")
    print("------------------------")