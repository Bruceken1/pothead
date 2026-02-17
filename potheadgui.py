import streamlit as st

st.set_page_config(page_title="Wholesale Profit Distribution", layout="wide")
st.title("📦 Wholesale Profit Distribution Calculator")

st.markdown("""
This app calculates investor profits and distributor profits in a wholesale model.
- Investors sell units to distributor at wholesale price
- Distributor can optionally share in investor profit
- Distributor resale profit can also be calculated
""")

# ================= STOCK & PRODUCTION =================
with st.container():
    st.header("1️⃣ Stock & Production")
    col1, col2 = st.columns(2)
    with col1:
        grams_purchased = float(st.text_input("Grams purchased", "0"))
        cost_per_gram = float(st.text_input("Cost per gram", "0"))
        total_cost = grams_purchased * cost_per_gram
    with col2:
        bags_produced = int(st.text_input("Number of bags produced", "0"))
        stks_produced = int(st.text_input("Number of stks produced", "0"))

# ================= WHOLESALE & EXPENSES =================
with st.container():
    st.header("2️⃣ Prices & Expenses")
    col1, col2 = st.columns(2)
    with col1:
        price_per_bag_wholesale = float(st.text_input("Wholesale price per bag", "0"))
        price_per_stk_wholesale = float(st.text_input("Wholesale price per stk", "0"))
    with col2:
        other_expenses = float(st.text_input("Other expenses", "0"))

# ================= DISTRIBUTOR OPTIONS =================
with st.container():
    st.header("3️⃣ Distributor Options")
    distributor_resell = st.checkbox("Calculate distributor resale profit?", value=False)
    distributor_share = st.checkbox("Distributor shares in investor profit?", value=False)
    if distributor_resell or distributor_share:
        col1, col2 = st.columns(2)
        with col1:
            commission_per_unit = float(st.text_input("Distributor commission per unit sold", "0"))
        with col2:
            if distributor_resell:
                price_per_bag_resell = float(st.text_input("Distributor resell price per bag", "0"))
                price_per_stk_resell = float(st.text_input("Distributor resell price per stk", "0"))

# ================= PARTNERS =================
with st.container():
    st.header("4️⃣ Investor Partners")
    num_partners = int(st.text_input("Number of investor partners", "2"))
    partner_percentages = []
    for i in range(num_partners):
        percent = float(st.text_input(f"Percentage for Partner {i+1}", "0"))
        partner_percentages.append(percent)
    if distributor_share:
        distributor_percent = float(st.text_input("Distributor's percentage share", "0"))
        partner_percentages.append(distributor_percent)
        num_partners += 1

# ================= CALCULATE =================
if st.button("💰 Calculate Profit Distribution"):

    total_units = bags_produced + stks_produced
    revenue_investors = bags_produced * price_per_bag_wholesale + stks_produced * price_per_stk_wholesale
    net_profit_investors = revenue_investors - total_cost - other_expenses

    st.subheader("📊 Investors Summary")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Revenue from distributor:", revenue_investors)
        st.write("Total Cost of Stock:", total_cost)
    with col2:
        st.write("Other Expenses:", other_expenses)
        st.write("Net Profit for Investors:", net_profit_investors)

    # Validate percentages
    if sum(partner_percentages) != 100:
        st.error("Percentages must sum to 100%")
    else:
        st.subheader("💵 Profit Distribution")
        for i, percent in enumerate(partner_percentages, start=1):
            amount = (percent / 100) * net_profit_investors
            if distributor_share and i == num_partners:
                st.write(f"Distributor gets (profit share): {amount}")
            else:
                st.write(f"Partner {i} gets: {amount}")

    # Distributor resale profit
    if distributor_resell:
        distributor_revenue = bags_produced * price_per_bag_resell + stks_produced * price_per_stk_resell
        distributor_purchase = revenue_investors
        distributor_profit = distributor_revenue - distributor_purchase
        st.subheader("💼 Distributor Resale Profit")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Revenue from reselling:", distributor_revenue)
        with col2:
            st.write("Amount paid to investors:", distributor_purchase)
            st.write("Net Profit:", distributor_profit)
