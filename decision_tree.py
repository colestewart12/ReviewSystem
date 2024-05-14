import numpy as np
import pandas as pd
from get_score_NLP import SentenceQuality
from sklearn.metrics import mean_squared_error

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTreeRegressor:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        num_samples, num_features = X.shape
        if num_samples >= self.min_samples_split and (self.max_depth is None or depth < self.max_depth):
            best_split = self._find_best_split(X, y, num_features)
            if best_split["mse"] < np.inf:
                left_subtree = self._build_tree(*best_split["left"], depth + 1)
                right_subtree = self._build_tree(*best_split["right"], depth + 1)
                return Node(best_split["feature"], best_split["threshold"], left_subtree, right_subtree)
        return Node(value=np.mean(y))

    def _find_best_split(self, X, y, num_features):
        best_split = {"mse": np.inf}
        for feature in range(num_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_indices = X[:, feature] <= threshold
                right_indices = X[:, feature] > threshold
                if len(np.unique(left_indices)) == 1 or len(np.unique(right_indices)) == 1:
                    continue
                mse = self._calculate_mse(y[left_indices], y[right_indices])
                if mse < best_split["mse"]:
                    best_split = {
                        "feature": feature,
                        "threshold": threshold,
                        "left": (X[left_indices], y[left_indices]),
                        "right": (X[right_indices], y[right_indices]),
                        "mse": mse,
                    }
        return best_split

    def _calculate_mse(self, left_y, right_y):
        left_mse = np.var(left_y) * len(left_y)
        right_mse = np.var(right_y) * len(right_y)
        mse = (left_mse + right_mse) / (len(left_y) + len(right_y))
        return mse

    def predict(self, X):
        return np.array([self._predict(inputs, self.root) for inputs in X])

    def _predict(self, inputs, node):
        if node.value is not None:
            return node.value
        if inputs[node.feature] <= node.threshold:
            return self._predict(inputs, node.left)
        else:
            return self._predict(inputs, node.right)
        

train_df = pd.read_csv('training_data.csv')
test_df = pd.read_csv('testing_data.csv')

sq = SentenceQuality()

train_features = [sq.calculateScores(row['text'], row['time_created'], row['weather']) for index, row in train_df.iterrows()]
train_scores = train_df['score'].values

test_features = [sq.calculateScores(row['text'], row['time_created'], row['weather']) for index, row in test_df.iterrows()]
test_scores = test_df['score'].values

X_train = np.array(train_features)
y_train = np.array(train_scores)
X_test = np.array(test_features)
y_test = np.array(test_scores)

tree_model = DecisionTreeRegressor(max_depth=5)
tree_model.fit(X_train, y_train)

train_predictions = tree_model.predict(X_train)
test_predictions = tree_model.predict(X_test)

#evaluating model
train_mse = mean_squared_error(y_train, train_predictions)
test_mse = mean_squared_error(y_test, test_predictions)
print(f"Training Data Mean Squared Error: {train_mse}")
print(f"Testing Data Mean Squared Error: {test_mse}")

def evaluate_predictions(y_true, y_pred, threshold=0.1):
    correct = np.abs(y_true - y_pred) <= threshold
    accuracy = np.mean(correct) * 100
    return accuracy

train_accuracy = evaluate_predictions(y_train, train_predictions, threshold=0.1)
test_accuracy = evaluate_predictions(y_test, test_predictions, threshold=0.1)
print(f"Training Data Accuracy: {train_accuracy}%")
print(f"Testing Data Accuracy: {test_accuracy}%")

def predict_review(tree_model, review, time_created, weather):
    sq = SentenceQuality()
    
    scores = sq.calculateScores(review, time_created, weather)
    
    features = np.array(scores).reshape(1, -1)
    
    predicted_score = tree_model.predict(features)
    
    return predicted_score[0]

review = "Just went here, great food and good portion. Love the kim chi box. The service and place was clean."
time_created = "2024-03-28 12:33:17"
weather = 58.658

predicted_score = predict_review(tree_model, review, time_created, weather)
print("Predicted quality score:", predicted_score)
