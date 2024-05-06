from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

iris = load_iris()
X_iris = iris.data
y_iris = iris.target
# X_iris, y_iris = load_iris(return_X_y=True)

X_train, X_validate, y_train, y_validate = train_test_split(X_iris, y_iris, test_size=0.5, random_state=42)

#model = GaussianNB()
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_predict = model.predict(X_validate)
print(accuracy_score(y_validate, y_predict))

scores = cross_val_score(model, X_iris, y_iris, cv=8)
print(scores.mean())

model_pca = PCA(n_components=2)
model_pca.fit(X_iris, y_iris)
X_PCA = model_pca.transform(X_iris)

plt.scatter(X_PCA[:, 0], X_PCA[:, 1], c=y_iris, alpha=0.5)
# plt.show()

model_gm = GaussianMixture(n_components=3)
model_gm.fit(X_iris)
y_gm = model_gm.predict(X_iris)
plt.scatter(X_PCA[:, 0], X_PCA[:, 1], c=y_gm, alpha=0.6)
plt.show()
