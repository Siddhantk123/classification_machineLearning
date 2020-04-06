

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#loading datasets
iris=datasets.load_iris()


#printing descreption and features of datasets
print(iris.DESCR)

features=iris.data
labels=iris.target

print(features[0],labels[0])

#training the model
#training the classifier

clf=KNeighborsClassifier()
clf.fit(features,labels)

#now predict the labels on the basis of new features input to it
prediction = clf.predict([[31,1,1,1]])
print(predict)

if prediction==1:
 print('Setosa')

elif prediction==1:
print('Versicolour')

else:
print('Virginica')




from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#loading datasets
iris=datasets.load_iris()


#printing descreption and features of datasets
print(iris.DESCR)

features=iris.data
labels=iris.target

print(features[0],labels[0])

#training the model
#training the classifier

clf=KNeighborsClassifier()
clf.fit(features,labels)

#now predict the labels on the basis of new features input to it
prediction = clf.predict([[31,1,1,1]])
print(prediction)

if prediction==1:
    print('Setosa')

elif prediction==2:
    print('Versicolour')

else:
    print('Virginica')


