# Code statements in order or input from the book:
# "Introduction to Machine Learning with Python" - Andreas C Muller & Sarah Guido
# a start on research for data science, Peter Cannon(PC)
# CHAPTER ONE: intro
from sklearn.datasets import load_iris #in9
iris_dataset = load_iris() #in9

print("Keys of iris_dataset: \n{}".format(iris_dataset.keys())) #in10

print(iris_dataset['DESCR'][:193] + "\n...") #in11

print("Target names: {}".format(iris_dataset['target_names'])) #in12

print("Feature names: \n{}".format(iris_dataset['feature_names'])) #in13

print("Type of data: {}".format(type(iris_dataset['data']))) #in14

print("Shape of the data: {}".format(iris_dataset['data'].shape)) #in15

print("First five rows of data:\n{}".format(iris_dataset['data'][:5])) #in16

print("Type of target: {}".format(type(iris_dataset['target']))) #in17

print("Shape of target: {}".format(iris_dataset['target'].shape)) #in18

print("Target:\n{}".format(iris_dataset['target'])) #in19

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0) #in20

print("x_train shape: {}".format(x_train.shape)) #in21
print("x_train shape: {}".format(y_train.shape)) 

print("x_test shape: {}".format(x_test.shape)) #in22
print("x_test shape: {}".format(y_test.shape)) 

# create dataframe from data in x_train
# label the columns using the strings in the iris_dataset.feature_news
iris_dataset = pd.DataFrame(x_train, columns = iris_dataset.feature_names)
# create a scatter matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(iris_dataframe, c = y_train, figsize = (15, 15), marker = 'o', hist_kwds = {'bins' : 20}, s = 60, alpha = .8, cmap = mglearn.cm3) #in23

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1) #in24

knn.fit(x_train, y_train) #in25

x_new = np.array([[5, 2.9, 1, 0.2]])
print("x_new.shape: {}".format(x_new.shape)) #in26

prediction = knn.predict(x_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(iris_dataset['target_names'][prediction])) #in27

y_pred = knn.predict(x_test)
print("Test set prediction:\n {}".format(y_pred)) #in28

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test))) #in29

print("Test set score: {:.2f}".format(knn.score(x_test, y_test))) #in30

x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)
knn = KNeighborsClassifier(n_neighbours = 1)
knn.fit(x_train, y_train)
print("Test set score: {:.2f}".format(knn.score(x_test, y_test))) #in31

# CHAPTER 2: supervised learning

