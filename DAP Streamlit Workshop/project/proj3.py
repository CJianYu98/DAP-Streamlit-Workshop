import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

def app():

    # Adding App Title
    st.title('Iris Flower Prediction App')

    # Add App description
    st.write("""
    This app predicts the **Iris flower** type based on user input sepal/petal measurements!
    """)

    # Creating a sidebar for user to adjust the parameter
    st.sidebar.header('Input Parameters')

    # Define a function to get user input
    def user_input_features():
        sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.7)
        data = {'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width}
        features = pd.DataFrame(data, index=[0])
        return features

    # Showing the input parameters
    df = user_input_features()

    st.subheader('User Input parameters')
    st.write(df)

    # Training our prediction models
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    st.subheader('Class labels and their corresponding index number')
    st.write(iris.target_names.reshape(1,3))

    models = []
    pred = []

    models.append(('Random Forest', RandomForestClassifier(max_depth=3, random_state=1)))
    models.append(('Gaussian Naive Bayes', GaussianNB()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('QDA', QuadraticDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier(n_neighbors = 3)))
    models.append(('Logistic Regression', LogisticRegression(solver = 'newton-cg')))
    models.append(('Linear SVC', SVC(kernel='linear')))

    for name, model in models:
        pred.append(iris.target_names[model.fit(X,Y).predict(df)])

    idx = [models[i][0] for i in range(len(models))]
    pred = pd.DataFrame(pred, columns = ['Prediction'], index = idx)

    # Show prediction for each model
    st.subheader('Prediction for each classifier')
    st.write(pred)

    # Show the prediction with the most votes
    st.subheader('Prediction from the majority of classifiers')
    st.write(pred['Prediction'].value_counts().index[0])