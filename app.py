import streamlit as st
import pickle

# load saved model
model = pickle.load(open('spam_model.pkl', 'rb'))

# load vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# app title
st.title("Spam Email Classifier")

# user input
email = st.text_area("Enter Email Message")

# prediction button
if st.button("Predict"):

    # convert text into numbers
    email_vector = vectorizer.transform([email])

    # predict
    prediction = model.predict(email_vector)

    # show result
    if prediction[0] == 1:
        st.error("Spam Email")
    else:
        st.success("Not Spam")