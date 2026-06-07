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
st.write("Calculate your exact payout or find your perfect selling price.")

st.write("---")

# ==========================================
# TOOL 1: FORWARD CALCULATOR (Calculate Payout)
# ==========================================
st.subheader("1️⃣ Calculate Payout")
st.caption("Find out exactly how much you will receive after fees.")

price = st.number_input("Product Selling Price (₱)", min_value=0.0, step=1.0, format="%.2f", key="forward_input")

if st.button("Calculate My Profit", type="primary", key="btn_forward"):
    if price > 0:
        # Math Logic
        shopee_fee = price * 0.27
        after_shopee = price - shopee_fee
        bir_fee = after_shopee * 0.03
        final_payout = after_shopee - bir_fee

        # Big, bold result
        st.success(f"Your Profit: ₱{final_payout:,.2f}")
        
        # Tappable drop-down for the breakdown
        with st.expander("View Math Breakdown"):
            st.markdown(f"""
            * **Selling Price:** ₱{price:,.2f}
            * **Shopee Fees (-27%):** -₱{shopee_fee:,.2f}
            * **Price after Shopee Fees:** ₱{after_shopee:,.2f}
            * **BIR Fee (-3%):** -₱{bir_fee:,.2f}
            """)
    else:
        st.warning("Please enter a price greater than 0.")

st.write("---")

# ==========================================
# TOOL 2: REVERSE CALCULATOR (Find Selling Price)
# ==========================================
st.subheader("2️⃣ Calculate Selling Price")
st.caption("Find out what to charge to cover all fees and hit your target.")

target_payout = st.number_input("Target Net Amount / Capital (₱)", min_value=0.0, step=1.0, format="%.2f", key="reverse_input")

if st.button("Calculate Target Price", type="primary", key="btn_reverse"):
    if target_payout > 0:
        # The Magic Number: 0.73 * 0.97 = 0.7081
        target_price = target_payout / 0.7081
        
        # Breakdown Math
        shopee_fee_rev = target_price * 0.27
        after_shopee_rev = target_price - shopee_fee_rev
        bir_fee_rev = after_shopee_rev * 0.03

        # Big, bold result
        st.info(f"### You should charge: ₱{target_price:,.2f}")
        
        # Tappable drop-down for the breakdown
        with st.expander("Verify the Math"):
            st.markdown(f"""
            * **If you sell it for:** ₱{target_price:,.2f}
            * **Shopee takes (-27%):** -₱{shopee_fee_rev:,.2f}
            * **Price after Shopee Fees:** ₱{after_shopee_rev:,.2f}
            * **BIR takes (-3%):** -₱{bir_fee_rev:,.2f}
            * **Final Net Amount:** **₱{target_payout:,.2f}**
            """)
    else:
        st.warning("Please enter an amount greater than 0.")
