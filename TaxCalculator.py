import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate tax for the Old Tax Regime in India
def calculate_tax_old(income, deductions):
    taxable_income = income - deductions
    tax = 0
    slab_details = []

    if taxable_income <= 250000:
        tax = 0
        slab_details.append(f"0% tax on ₹{taxable_income}")
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
        slab_details.append(f"5% tax on ₹{taxable_income - 250000}")
    elif taxable_income <= 1000000:
        tax = (taxable_income - 500000) * 0.2 + 12500
        slab_details.append(f"20% tax on ₹{taxable_income - 500000}")
    else:
        tax = (taxable_income - 1000000) * 0.3 + 112500
        slab_details.append(f"30% tax on ₹{taxable_income - 1000000}")

    post_tax_income = taxable_income - tax
    return taxable_income, tax, post_tax_income, slab_details

# Function to calculate tax for the New Tax Regime in India
def calculate_tax_new(income, deductions):
    # In the new regime, most deductions are removed
    taxable_income = income
    tax = 0
    slab_details = []

    if taxable_income <= 250000:
        tax = 0
        slab_details.append(f"0% tax on ₹{taxable_income}")
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
        slab_details.append(f"5% tax on ₹{taxable_income - 250000}")
    elif taxable_income <= 1000000:
        tax = (taxable_income - 500000) * 0.2 + 12500
        slab_details.append(f"20% tax on ₹{taxable_income - 500000}")
    else:
        tax = (taxable_income - 1000000) * 0.3 + 112500
        slab_details.append(f"30% tax on ₹{taxable_income - 1000000}")

    post_tax_income = taxable_income - tax
    return taxable_income, tax, post_tax_income, slab_details

# Function for tax saving suggestions
def tax_saving_suggestions():
    st.write("""
    **Tax Saving Suggestions**:
    - Consider investing in **ELSS** (Equity Linked Savings Schemes) under section 80C.
    - You can invest in **PPF** (Public Provident Fund) for tax-free returns.
    - Opt for **Health Insurance** under section 80D to claim deductions.
    - Contribute to **NPS** (National Pension Scheme) to reduce taxable income.
    - Donations under section 80G can also help save taxes.
    """)

# Function for graphical representation (Bar chart)
def plot_graph(income, tax, deductions):
    categories = ['Income', 'Tax', 'Deductions']
    values = [income, tax, deductions]

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['green', 'red', 'blue'])
    ax.set_ylabel('₹ Amount')
    ax.set_title('Income, Tax, and Deductions Breakdown')
    plt.tight_layout()

    st.pyplot(fig)

# Function to calculate tax for the USA
def calculate_tax_usa(income):
    tax = 0
    slab_details = []

    if income <= 9950:
        tax = income * 0.1
        slab_details.append(f"10% tax on ${income}")
    elif income <= 40525:
        tax = (income - 9950) * 0.12 + 995
        slab_details.append(f"12% tax on ${income - 9950}")
    elif income <= 86375:
        tax = (income - 40525) * 0.22 + 4664
        slab_details.append(f"22% tax on ${income - 40525}")
    else:
        tax = (income - 86375) * 0.24 + 14751
        slab_details.append(f"24% tax on ${income - 86375}")

    post_tax_income = income - tax
    return tax, post_tax_income, slab_details

# Function to calculate tax for the UK
def calculate_tax_uk(income):
    tax = 0
    slab_details = []

    if income <= 12570:
        tax = 0
        slab_details.append(f"0% tax on £{income}")
    elif income <= 50270:
        tax = (income - 12570) * 0.2
        slab_details.append(f"20% tax on £{income - 12570}")
    elif income <= 150000:
        tax = (income - 50270) * 0.4 + 7540
        slab_details.append(f"40% tax on £{income - 50270}")
    else:
        tax = (income - 150000) * 0.45 + 54172
        slab_details.append(f"45% tax on £{income - 150000}")

    post_tax_income = income - tax
    return tax, post_tax_income, slab_details

# Function to calculate tax for Australia
def calculate_tax_aus(income):
    tax = 0
    slab_details = []

    if income <= 18200:
        tax = 0
        slab_details.append(f"0% tax on ${income}")
    elif income <= 45000:
        tax = (income - 18200) * 0.19
        slab_details.append(f"19% tax on ${income - 18200}")
    elif income <= 120000:
        tax = (income - 45000) * 0.325 + 5092
        slab_details.append(f"32.5% tax on ${income - 45000}")
    else:
        tax = (income - 120000) * 0.37 + 29467
        slab_details.append(f"37% tax on ${income - 120000}")

    post_tax_income = income - tax
    return tax, post_tax_income, slab_details

# Streamlit UI
def main():
    # Title of the app
    st.title("Tax Calculator")

    # Country Selection
    country = st.selectbox("Select your Country:", ["India", "USA", "UK", "Australia"])

    # User input for multiple income sources and deductions
    salary = st.number_input("Enter your Salary Income :", min_value=0, step=5000)
    rental_income = st.number_input("Enter your Rental Income :", min_value=0, step=5000)
    other_income = st.number_input("Enter other Income :", min_value=0, step=5000)
    deductions = st.number_input("Enter your Deductions :", min_value=0, step=5000)
    
    # Total Income Calculation
    total_income = salary + rental_income + other_income

    
    if country == "India":
        # Tax Regime Selection for India
        tax_regime = st.radio("Select Tax Regime:", ("Old Tax Regime", "New Tax Regime"))

        if tax_regime == "Old Tax Regime":
            if st.button('Calculate Tax (Old Regime)'):
                taxable_income, tax, post_tax_income, slab_details = calculate_tax_old(total_income, deductions)

                # Display Results
                st.write(f"**Taxable Income**: ₹{taxable_income}")
                st.write(f"**Tax Amount**: ₹{tax}")
                st.write(f"**Post-tax Income**: ₹{post_tax_income}")

                # Show tax slab breakdown
                st.write("**Tax Slab Breakdown**:")
                for detail in slab_details:
                    st.write(detail)
                
                # Graphical representation
                plot_graph(total_income, tax, deductions)
                
                # Show tax saving suggestions
                tax_saving_suggestions()

        elif tax_regime == "New Tax Regime":
            if st.button('Calculate Tax (New Regime)'):
                taxable_income, tax, post_tax_income, slab_details = calculate_tax_new(total_income, deductions)

                # Display Results
                st.write(f"**Taxable Income**: ₹{taxable_income}")
                st.write(f"**Tax Amount**: ₹{tax}")
                st.write(f"**Post-tax Income**: ₹{post_tax_income}")

                # Show tax slab breakdown
                st.write("**Tax Slab Breakdown**:")
                for detail in slab_details:
                    st.write(detail)
                
                # Graphical representation
                plot_graph(total_income, tax, deductions)
                
                # Show tax saving suggestions
                tax_saving_suggestions()

    elif country == "USA":
        if st.button('Calculate Tax for USA'):
            tax, post_tax_income, slab_details = calculate_tax_usa(total_income)

            # Display Results
            st.write(f"**Tax Amount**: ${tax}")
            st.write(f"**Post-tax Income**: ${post_tax_income}")

            # Show tax slab breakdown
            st.write("**Tax Slab Breakdown**:")
            for detail in slab_details:
                st.write(detail)

    elif country == "UK":
        if st.button('Calculate Tax for UK'):
            tax, post_tax_income, slab_details = calculate_tax_uk(total_income)

            # Display Results
            st.write(f"**Tax Amount**: £{tax}")
            st.write(f"**Post-tax Income**: £{post_tax_income}")

            # Show tax slab breakdown
            st.write("**Tax Slab Breakdown**:")
            for detail in slab_details:
                st.write(detail)

    elif country == "Australia":
        if st.button('Calculate Tax for Australia'):
            tax, post_tax_income, slab_details = calculate_tax_aus(total_income)

            # Display Results
            st.write(f"**Tax Amount**: ${tax}")
            st.write(f"**Post-tax Income**: ${post_tax_income}")

            # Show tax slab breakdown
            st.write("**Tax Slab Breakdown**:")
            for detail in slab_details:
                st.write(detail)

if __name__ == "__main__":
    main()
