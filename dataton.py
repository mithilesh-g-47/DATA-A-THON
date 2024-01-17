# -*- coding: utf-8 -*-
"""dataton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1crtJaGAdNNs2QqHWYUvmCfYI1TF9u3LM
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv('bank (6) (1).csv')
print(data.head())

print(data.columns)

#Exploratory Data Analysis (EDA)
#Data Summary:
print(data.describe())

##Analysis of Categorical Features:
data['job'] = data['job'].astype('category')
plt.figure(figsize=(10, 6))

sns.countplot(data=data, x='job', order=data['job'].value_counts().index)
plt.xticks(rotation=80)
plt.xlabel('Job')
plt.ylabel('Count')
plt.title('Job Distribution')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='marital', order=data['marital'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('marital')
plt.ylabel('Count')
plt.title('marital status')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='education', order=data['education'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('education')
plt.ylabel('Count')
plt.title('education')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='default', order=data['default'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('default')
plt.ylabel('Count')
plt.title('default')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='housing', order=data['housing'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('housing')
plt.ylabel('Count')
plt.title('housing')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='loan', order=data['loan'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('loan')
plt.ylabel('Count')
plt.title('loan')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='contact', order=data['contact'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('contact')
plt.ylabel('Count')
plt.title('contact')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='month', order=data['month'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('month')
plt.ylabel('Count')
plt.title('month')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='day_of_week', order=data['day_of_week'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('day_of_week')
plt.ylabel('Count')
plt.title('day_of_week')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='poutcome', order=data['poutcome'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('poutcome')
plt.ylabel('Count')
plt.title('poutcome')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='y', order=data['y'].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel('y')
plt.ylabel('Count')
plt.title('Subscription to term deposit')
plt.show()

numerical_columns = ['age', 'duration', 'campaign', 'pdays', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']

# Create subplots for each numerical column
plt.figure(figsize=(16, 10))

for i, column in enumerate(numerical_columns):
    plt.subplot(3, 4, i + 1)
    plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'{column} Histogram')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Create a mask to hide the upper triangular part of the plot:
correlation_matrix = data.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Settin up the matplotlib figure
plt.figure(figsize=(12, 10))

# Customizing the color map
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Creating  the heatmap with annotations and a color bar
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": 0.75})

# Adding  the title
plt.title("Correlation Heatmap")

# Displaying the plot
plt.show()

#2. Feature Engineering
# a) Missing Value Treatment
data.dropna(inplace=True)

#b) Label Encoding
label_encoder = LabelEncoder()
categorical_columns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']
for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column])

# c) Imbalanced Data Handling (using SMOTE)
X = data.drop(columns=['y'])
y = data['y']
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

#Missing values were handled by dropna method
#Categorical variables were encoded using label encoding.
#Imbalanced data was addressed using SMOTE(Synthetic Minority Over-sampling Technique), resulting in a balanced dataset.

#SLOT 2

#building three supervised learning models- random forest classifier , Logistic Regression, Decision Tree Classifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix



# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# MODEL 1 : Random forest classifier:
#For testing the performance of the data model
y_pred = clf.predict(X_test)


from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
print("Confusion Matrix:")
print(confusion)

# Model 2: Logistic Regression
logistic_model = LogisticRegression(max_iter=10000, random_state=42)
logistic_model.fit(X_train, y_train)
y_pred_logistic = logistic_model.predict(X_test)

# Model 3: Decision Tree Classifier
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
y_pred_tree = tree_model.predict(X_test)



# Evaluating Model 2 (Logistic Regression)
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)
report_logistic = classification_report(y_test, y_pred_logistic)
confusion_logistic = confusion_matrix(y_test, y_pred_logistic)

# Evaluating Model 3 (Decision Tree Classifier)
accuracy_tree = accuracy_score(y_test, y_pred_tree)
report_tree = classification_report(y_test, y_pred_tree)
confusion_tree = confusion_matrix(y_test, y_pred_tree)



# Printing evaluation metrics for each model
print("Model 2: Logistic Regression")
print("Accuracy:", accuracy_logistic)
print("\nClassification Report:")
print(report_logistic)
print("\nConfusion Matrix:")
print(confusion_logistic)

print("\nModel 3: Decision Tree Classifier")
print("Accuracy:", accuracy_tree)
print("\nClassification Report:")
print(report_tree)
print("\nConfusion Matrix:")
print(confusion_tree)