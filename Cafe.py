import streamlit as st

# Initialize session state for cart if not already present
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Sample Menu Data
menu_data = {
    "Coffee": [
        ("Espresso", 2.5,),
        ("Cappuccino", 3.5),
        ("Latte", 4.0),
        ("Mocha", 4.5),
    ],
    "Bakery": [
        ("Croissant", 2.0),
        ("Muffin", 2.5),
        ("Bagel", 2.8),
    ],
    "Pizza": [
        ("Margherita Pizza", 8.0),
        ("Pepperoni Pizza", 9.5),
        ("Veggie Pizza", 9.0),
    ],
    "Pasta": [
        ("Pasta Alfredo", 7.5),
        ("Pasta Bolognese", 8.5),
        ("Pesto Pasta", 7.8),
    ],
    "Dessert": [
        ("Chocolate Cake", 5.0),
        ("Cheesecake", 5.5),
        ("Ice Cream Sundae", 4.0),
    ]
}

# Page Navigation
st.sidebar.title("🍽️ Navigate")
page = st.sidebar.radio("Where would you like to go?", ["🏠 Home", "📜 Menu", "🛒 Order", "🛍️ Cart", "📞 Contact Us"])

if page == "🏠 Home":
    st.title("Welcome to Luxurious Café ☕🍰")
    st.image("h.jpg", width=500)
    st.image("hg.jpg", width=300)
    st.image("jh.jpg", width=500)
    st.image("es.jpeg", width=300)
    st.image("mocha.jpeg", width=500)
    st.image("ca.jpg", width=300)
    st.write(
        "Step into a world of rich aromas, delicious treats, and an ambiance crafted for comfort and indulgence. Take your time browsing through our menu and place your order when you're ready!")
    st.write(
        "Welcome to a place where every meal is a masterpiece and every moment is a celebration. Sit back, relax, and let the aromas of freshly brewed coffee and baked delicacies transport you to a world of pure indulgence.")

elif page == "📜 Menu":
    st.title("Our Delicious Menu")
    theme = st.selectbox("Choose a Theme for Your Experience", ["Classic", "Modern", "Vintage"])
    category = st.selectbox("Select a Category", list(menu_data.keys()))

    st.write("### Here’s What We Offer:")
    for item, price in menu_data[category]:
        st.write(f"**{item}** - 💲{price:.2f}")
        if st.button(f"Add {item} to Cart", key=item):
            if item in st.session_state.cart:
                st.session_state.cart[item]['quantity'] += 1
            else:
                st.session_state.cart[item] = {'price': price, 'quantity': 1}
            st.success(f"{item} added to cart!")

elif page == "🛒 Order":
    st.title("Place Your Order")
    category = st.selectbox("Pick a Category", list(menu_data.keys()))

    for item, price in menu_data[category]:
        quantity = st.number_input(f"How many {item}(s)?", min_value=1, max_value=10, value=1, key=item)
        if st.button(f"Add {quantity} {item}(s) to Cart", key=f"order_{item}"):
            if item in st.session_state.cart:
                st.session_state.cart[item]['quantity'] += quantity
            else:
                st.session_state.cart[item] = {'price': price, 'quantity': quantity}
            st.success(f"Added {quantity} {item}(s) to cart!")

elif page == "🛍️ Cart":
    st.title("Your Shopping Cart")
    if not st.session_state.cart:
        st.write("Your cart is looking a little empty! Add some delicious treats from our menu.")
    else:
        total_price = 0
        for item, details in st.session_state.cart.items():
            st.write(
                f"**{item}** - 💲{details['price']} x {details['quantity']} = 💲{details['price'] * details['quantity']}")
            total_price += details['price'] * details['quantity']
        st.write(f"### Total: 💲{total_price:.2f}")
        if st.button("Place Order"):
            st.session_state.cart.clear()
            st.success("Your order has been placed successfully! Enjoy your meal. 🍽️")

elif page == "📞 Contact Us":
    st.title("Get in Touch with Us")
    st.write(
        "We love hearing from our customers! Whether you have a question, feedback, or just want to say hi, drop us a message below.")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        st.success("Thanks for reaching out! We’ll get back to you as soon as possible.")
