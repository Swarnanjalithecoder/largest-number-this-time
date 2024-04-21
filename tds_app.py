import streamlit as st

def find_largest_number(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    st.title("Find the Largest Number")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest Number"):
        largest = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest}")


