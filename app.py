import streamlit as st

# Configure the page
st.set_page_config(page_title="Shopee Calculator", page_icon="🛍️", layout="centered")

# CSS Injection for Mobile Optimization (Larger buttons)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🛍️ Shopee Calculator")
st.write("Calculate your exact profit or find your perfect selling price.")

st.write("---")

# ==========================================
# TOOL 1: FORWARD CALCULATOR (Calculate Profit)
# ==========================================
st.subheader("1️⃣ Calculate Profit")
st.caption("Find out exactly how much you will receive after fees.")

# Setting value=None makes the box blank initially
price = st.number_input("Product Selling Price (₱)", min_value=0.0, step=1.0, format="%.2f", value=None, placeholder="Enter price...", key="forward_input")

if st.button("Calculate My Profit", type="primary", key="btn_forward"):
    # We must check if price is not None before doing the math
    if price is not None and price > 0:
        # Math Logic
        shopee_fee = price * 0.27
        after_shopee = price - shopee_fee
        bir_fee = after_shopee * 0.03
        final_profit = after_shopee - bir_fee

        # Standardized green success box
        st.success(f"### Net Profit: ₱{final_profit:,.2f}")
        
        # Standardized receipt breakdown
        with st.expander("View Math Breakdown"):
            st.markdown(f"""
            * **Base Amount:** ₱{price:,.2f}
            * **Shopee Fees (-27%):** -₱{shopee_fee:,.2f}
            * **Price after Shopee:** ₱{after_shopee:,.2f}
            * **BIR WHT (-3%):** -₱{bir_fee:,.2f}
            * **Final Net Amount:** **₱{final_profit:,.2f}**
            """)
    else:
        st.warning("Please enter a valid amount.")

st.write("---")

# ==========================================
# TOOL 2: REVERSE CALCULATOR (Find Selling Price)
# ==========================================
st.subheader("2️⃣ Calculate Selling Price")
st.caption("Find out what to charge to cover all fees and hit your target.")

# Setting value=None makes the box blank initially
target_profit = st.number_input("Target Net Amount / Capital (₱)", min_value=0.0, step=1.0, format="%.2f", value=None, placeholder="Enter target amount...", key="reverse_input")

if st.button("Calculate Target Price", type="primary", key="btn_reverse"):
    # We must check if target_profit is not None before doing the math
    if target_profit is not None and target_profit > 0:
        # The Magic Number: 0.73 * 0.97 = 0.7081
        target_price = target_profit / 0.7081
        
        # Breakdown Math
        shopee_fee_rev = target_price * 0.27
        after_shopee_rev = target_price - shopee_fee_rev
        bir_fee_rev = after_shopee_rev * 0.03

        # Standardized green success box matching Tool 1
        st.success(f"### You should charge: ₱{target_price:,.2f}")
        
        # Standardized receipt breakdown matching Tool 1
        with st.expander("View Math Breakdown"):
            st.markdown(f"""
            * **Base Amount:** ₱{target_price:,.2f}
            * **Shopee Fees (-27%):** -₱{shopee_fee_rev:,.2f}
            * **Price after Shopee:** ₱{after_shopee_rev:,.2f}
            * **BIR WHT (-3%):** -₱{bir_fee_rev:,.2f}
            * **Final Net Amount:** **₱{target_profit:,.2f}**
            """)
    else:
        st.warning("Please enter a valid amount.")
