import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Load the trained model
model = pickle.load(open('model1.sav', 'rb'))

# Streamlit app
st.title("Online Payments Fraud Detection")

# Get user input
transaction_type = st.selectbox("Select the type of transaction", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
amount = st.number_input("Enter the amount", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("Enter the balance before transaction", min_value=0.0, step=0.01)
newbalanceOrig = st.number_input("Enter the balance after transaction", min_value=0.0, step=0.01)

# Convert the transaction type to a numeric value
transaction_type_map = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
transaction_type_num = transaction_type_map[transaction_type]

# Create the input data
input_data = [[transaction_type_num, amount, oldbalanceOrg, newbalanceOrig]]

# Make the prediction
if st.button("Detect Fraud"):
    prediction = model.predict(input_data)
    if prediction[0] == "Fraud":
        st.success("Flagged as Fraud")
    else:
        st.success("Flagged as Not Fraud")