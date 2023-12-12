import pandas as pd
import os 
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

csv_file_path = os.path.join('main', 'finaldataset.csv')
data = pd.read_csv(csv_file_path)

def proses(input):
    X1=data.iloc[:, 0:10]
    y1=data['Cluster_enc']
    X_train, X_test, y_train, y_test=train_test_split(X1,y1,test_size=.3,random_state=0)
    clf=GaussianNB()
    clf.fit(X_train, y_train)
    y_pred=clf.predict(X_test)
    y_pred_dt = clf.predict(X_test)
    all_predictions = clf.predict(input)
    
    return all_predictions
