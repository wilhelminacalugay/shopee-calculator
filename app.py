import streamlit as st

# Configure the page
st.set_page_config(page_title="Shopee Fee Calculator", page_icon="🛍️")

# App Header
st.title("Shopee Payout Calculator 🛍️")
st.write("Calculate your net dues after Shopee and BIR deductions.")

# Input Field
price = st.number_input("Product Price (₱)", min_value=0.0, step=1.0, format="%.2f")

# Calculate Button
if st.button("Calculate Payout", type="primary"):
    if price > 0:
        # Math Logic
        shopee_fee = price * 0.27
        after_shopee = price - shopee_fee
        bir_fee = after_shopee * 0.03
        final_payout = after_shopee - bir_fee

        # Display Results
        st.divider()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Shopee Fees (-27%):**")
            st.write("**Price after Shopee:**")
            st.write("**BIR WHT (-3%):**")
            
        with col2:
            st.write(f"₱{shopee_fee:,.2f}")
            st.write(f"₱{after_shopee:,.2f}")
            st.write(f"₱{bir_fee:,.2f}")
            
        st.success(f"**Your Net Dues:** ₱{final_payout:,.2f}")
    else:
        st.warning("Please enter a price greater than 0.")
