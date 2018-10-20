from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection

validation_size = 0.33

seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(XX, yy, test_size=validation_size, random_state=seed)
clf = GaussianNB()
clf.fit(X_train, Y_train)
scoring = 'accuracy'
kfold = model_selection.KFold(n_splits=10, random_state=seed)

cv_results = model_selection.cross_val_score(GaussianNB(), X_train, Y_train, cv=kfold, scoring=scoring)
cv_results_V = model_selection.cross_val_score(GaussianNB(), X_validation, Y_validation, cv=kfold, scoring=scoring)

print('The accuracy of the Naive Bayes classifier on training data is {:.2f}'.format(cv_results.mean()))
print('The accuracy of the Naive Bayes classifier on test data is {:.2f}'.format(cv_results_V.mean()))


