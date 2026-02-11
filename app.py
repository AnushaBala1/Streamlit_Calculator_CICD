import streamlit as st

st.set_page_config(page_title="Calculator App", layout="centered")

st.title("Simple Calculator – CI/CD Demo")
st.write("This calculator application is deployed using Jenkins CI/CD pipeline.")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculation logic
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed")

    if result is not None:
        st.success(f"Result: {result}")