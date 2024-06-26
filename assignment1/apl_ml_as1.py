import pandas as pd
from sklearn.datasets import load_wine
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from itertools import combinations

# Load the wine dataset
wine = load_wine()

# Convert to DataFrame
wine_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
# make a column for the labels
wine_df['label'] = wine.target

ratio = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print(f"Number of samples: {wine_df.shape[0]}")
print(f"Number of features: {len(wine.feature_names)}")

print("\nFeature ranges:")
print(wine_df.max() - wine_df.min())

print("\nFeature scales (standard deviation):")
print(wine_df.std())

print("\nFeature variances:")
print(wine_df.var())

X = wine_df.iloc[:, :-1]
y = wine_df.iloc[:, -1]

accuracies = []

for r in ratio:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=r)
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

plt.plot(ratio, accuracies)
plt.xlabel('Test Size Ratio')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Test Size Ratio')
plt.grid(True)
plt.show()

# Finding the minimum label count
label_counts = wine_df['label'].value_counts()
lmin = label_counts.min()

# Create an empty DataFrame for the balanced
balanced_wine = pd.DataFrame(columns=wine_df.columns)

# For each label, randomly select lmin samples and add to the new datafarme
for label in label_counts.index:
    label_df = wine_df[wine_df['label'] == label]
    label_df_min = label_df.sample(n=lmin)

    balanced_wine = pd.concat([balanced_wine, label_df_min])

# Convert the label to an integer
balanced_wine['label'] = balanced_wine['label'].astype(int)


# Split the data to X and y
X = balanced_wine.iloc[:, :-1]
y = balanced_wine.iloc[:, -1]

# Split the data to train and test
accuracy_arr = []
for i in ratio:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=i)
    # Train logistic regression model
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    # prediction
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    accuracy_arr.append(accuracy)

print("The accuracy of the balanced_wine data is: \n")
for i, j in zip(ratio, accuracy_arr):
    print(f"for r = {i}: {j}")

def k_features_selection(train_set, test_set,k):

    accuracy_max = 0
    features_max = None

    train_set_x = train_set.iloc[:, :-1]
    train_set_y = train_set.iloc[:, -1]
    test_set_x = test_set.iloc[:, :-1]
    test_set_y = test_set.iloc[:, -1]

    # get the features differnt combinations
    features = train_set_x.columns
    combinations_options = list(combinations(features, k))

    #check what is the best combination
    for option in combinations_options:
        arr_option = np.array(option)
        train_set_x_new = train_set_x[arr_option]
        test_set_x_new = test_set_x[arr_option]

        model = LogisticRegression(max_iter=1000)
        model.fit(train_set_x_new, train_set_y)

        # prediction
        pred = model.predict(test_set_x_new)
        accuracy = accuracy_score(test_set_y, pred)

        if accuracy>accuracy_max:
            accuracy_max = accuracy
            features_max = option

    return features_max, accuracy_max


train_set, test_set, = train_test_split(wine_df, test_size=0.1)

features_max, accuracy_max = k_features_selection(train_set, test_set,2)
print(f"the best features are: {features_max} with accuracy: {accuracy_max}")
