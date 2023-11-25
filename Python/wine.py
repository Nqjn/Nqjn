import pandas as pd
from sklearn import tree, datasets
from typing import Optional
wine = datasets.load_wine()
def create_wine_tree() -> tree.DecisionTreeClassifier:

    
    X = wine.data[:, [0, 1, 4, 6]] 
    y = wine.target


    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, y)
    
    return clf

def predict_samples(clf: tree.DecisionTreeClassifier,
                    wine_parameters: list[list[float]]) -> Optional[list[int]]:

    if not wine_parameters or not all(len(sample) == 4 for sample in wine_parameters):
        return None

    return clf.predict(wine_parameters).tolist()

# Testy:
clf = create_wine_tree()
print(predict_samples(clf, [[12.8, 0.76, 79.3, 0.38], [13.5, 2.38, 103.5, 2.41]]))    # [1, 0]
print(predict_samples(clf, [[11.6, 3.15, 114.3]]))    # None

df = pd.DataFrame(wine.data, columns=wine.feature_names)

# Zobrazení datového rámce
print(df)