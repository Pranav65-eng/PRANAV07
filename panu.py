import streamlit as st
import pandas as pd

# Create a sample sales ledger DataFrame
data = {
    'Date': ['2023-10-26', '2023-10-26', '2023-10-26', '2023-10-27', '2023-10-27'],
    'Item': ['Apple', 'Banana', 'Milk', 'Bread', 'Eggs'],
    'Quantity': [5, 3, 2, 1, 12],
    'Unit Price': [0.75, 0.25, 3.50, 2.00, 2.50],
    'Total Price': [3.75, 0.75, 7.00, 2.00, 30.00]
}

sales_ledger = pd.DataFrame(data)

# Display the sales ledger as a table in Streamlit
st.title("Sales Ledger")
st.write(sales_ledger)

# Calculate total sales for each day
daily_sales = sales_ledger.groupby('Date')['Total Price'].sum()

# Display total sales by date
st.subheader("Total Sales by Date")
st.write(daily_sales)

# Calculate total sales for each item
item_sales = sales_ledger.groupby('Item')['Total Price'].sum()

# Display total sales by item
st.subheader("Total Sales by Item")
st.write(item_sales)
