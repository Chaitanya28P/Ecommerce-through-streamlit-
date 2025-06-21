
import streamlit as st

st.set_page_config(page_title="E-Commerce App", layout="centered")
st.title(" E-Commerce Store")

# Use session state to hold the total and selections
if "total" not in st.session_state:
    st.session_state.total = 0

st.sidebar.header("Cart")
st.sidebar.write(f"**Total Amount:** ₹{st.session_state.total}")

# Main category selection
category = st.selectbox("Choose a category:", [
    "Select",
    "Clothes",
    "Home Appliances",
    "Outdoor",
    "Jewellery",
    "Study Material",
    "Checkout"
])

if category == "Clothes":
    gender = st.radio("Select Gender:", ["Mens", "Ladies", "Kids"])

    if gender == "Mens":
        mens_type = st.selectbox("Select Menswear Category", ["Select", "Traditional", "Formals", "Comfort"])
        if mens_type == "Traditional":
            item = st.radio("Choose item:", ["Kurtas ₹799", "Sherwani ₹2999"])
            if st.button("Add to Cart - Mens Traditional"):
                if item == "Kurtas ₹799":
                    st.session_state.total += 799
                elif item == "Sherwani ₹2999":
                    st.session_state.total += 2999
                st.success(f" {item} added to cart!")

        elif mens_type == "Formals":
            item = st.radio("Choose item:", ["Shirt ₹699", "Pant ₹500", "Semi-formal (Shirt+Pant) ₹999"])
            if st.button("Add to Cart - Mens Formals"):
                if item == "Shirt ₹699":
                    st.session_state.total += 699
                elif item == "Pant ₹500":
                    st.session_state.total += 500
                elif item == "Semi-formal (Shirt+Pant) ₹999":
                    st.session_state.total += 999
                st.success(f" {item} added to cart!")

        elif mens_type == "Comfort":
            item = st.radio("Choose item:", ["Boxer+Stinger ₹699", "T-shirt ₹499"])
            if st.button("Add to Cart - Mens Comfort"):
                if item == "Boxer+Stinger ₹699":
                    st.session_state.total += 699
                elif item == "T-shirt ₹499":
                    st.session_state.total += 499
                st.success(f" {item} added to cart!")

    elif gender == "Ladies":
        ladies_type = st.selectbox("Select Category", ["Select", "Traditional", "Western"])
        if ladies_type == "Traditional":
            item = st.radio("Choose:", ["Saree ₹1299", "Lehenga ₹2499"])
            if st.button("Add to Cart - Ladies Traditional"):
                if item == "Saree ₹1299":
                    st.session_state.total += 1299
                elif item == "Lehenga ₹2499":
                    st.session_state.total += 2499
                st.success(f" {item} added to cart!")

        elif ladies_type == "Western":
            item = st.radio("Choose:", ["Dress ₹999", "Jeans+Top ₹899"])
            if st.button("Add to Cart - Ladies Western"):
                if item == "Dress ₹999":
                    st.session_state.total += 999
                elif item == "Jeans+Top ₹899":
                    st.session_state.total += 899
                st.success(f" {item} added to cart!")

    elif gender == "Kids":
        item = st.radio("Choose item:", ["Shirt ₹399", "Lower ₹499", "Shorts ₹299"])
        if st.button("Add to Cart - Kids"):
            if item == "Shirt ₹399":
                st.session_state.total += 399
            elif item == "Lower ₹499":
                st.session_state.total += 499
            elif item == "Shorts ₹299":
                st.session_state.total += 299
            st.success(f" {item} added to cart!")

elif category == "Home Appliances":
    item = st.selectbox("Select Appliance", ["Select", "TV", "Fridge", "AC", "Washing Machine"])
    if item == "TV":
        opt = st.radio("Choose:", ["LED ₹15999", "Smart ₹25999", "4K ₹35999"])
    elif item == "Fridge":
        opt = st.radio("Choose:", ["Single Door ₹10000", "Double Door ₹20000", "Smart Fridge ₹28000"])
    elif item == "AC":
        opt = st.radio("Choose:", ["1 Ton ₹2000", "1.5 Ton ₹2100", "2 Ton ₹3000"])
    elif item == "Washing Machine":
        opt = st.radio("Choose:", ["Semi-Automatic ₹8000", "Fully-Automatic ₹1000", "Front Load ₹2000"])
    else:
        opt = None

    if opt and st.button("Add to Cart - Appliance"):
        price = int(opt.split("₹")[-1])
        st.session_state.total += price
        st.success(f" {opt} added to cart!")

elif category == "Outdoor":
    item = st.radio("Choose item:", ["Badminton ₹599", "Football ₹799", "Cricket Bat ₹1099"])
    if st.button("Add to Cart - Outdoor"):
        price = int(item.split("₹")[-1])
        st.session_state.total += price
        st.success(f" {item} added to cart!")

elif category == "Jewellery":
    item = st.radio("Choose:", ["Chain ₹1500", "Ring ₹23200", "Earring ₹50", "Necklace ₹999"])
    if st.button("Add to Cart - Jewellery"):
        price = int(item.split("₹")[-1])
        st.session_state.total += price
        st.success(f"{item} added to cart!")

elif category == "Study Material":
    choice = st.selectbox("Select:", ["Select", "Book", "Pen"])
    if choice == "Book":
        item = st.radio("Choose:", ["Notebook ₹69", "Journal Book ₹129"])
    elif choice == "Pen":
        item = st.radio("Choose:", ["Blue ₹10", "Black ₹12"])
    else:
        item = None

    if item and st.button("Add to Cart - Study Material"):
        price = int(item.split("₹")[-1])
        st.session_state.total += price
        st.success(f" {item} added to cart!")

elif category == "Checkout":
    st.header("Checkout")
    st.success(f"Your total bill is ₹{st.session_state.total}")
    if st.button("Reset Cart"):
        st.session_state.total = 0
        st.experimental_rerun()

