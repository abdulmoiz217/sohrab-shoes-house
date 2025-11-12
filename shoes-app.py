import streamlit as st

st.title("Sohrab Shoes House")
st.subheader("Find your best shoes in wholesale at reasonable price")
st.image("sohrab godam card.jpg")
st.text("Contact us for more info and buy shoes")

options = st.sidebar.radio("Options", ["home", "collection", "contact"])

if options == "home":
    nike, adidas = st.columns(2)

    with nike:
        st.subheader("Your Dream Nike")
        st.image("https://up.yimg.com/ib/th/id/OIP.tAZtpLwas9yqBLsTpL9-5QHaEK?pid=Api&rs=1&c=1&qlt=95&w=196&h=110", width=300)
        st.image("https://up.yimg.com/ib/th/id/OIP.x87oBIWS3WG_v-CsfvJNeAHaFL?pid=Api&rs=1&c=1&qlt=95&w=169&h=118", width=300)

    with adidas:
        st.subheader("Your Dream Adidas")
        st.image("https://up.yimg.com/ib/th/id/OIP.EcpWVgVvTUz7bM8Ddq1xQwHaHa?pid=Api&rs=1&c=1&qlt=95&w=121&h=121", width=200)
        st.image("https://up.yimg.com/ib/th/id/OIP.Rgk0bUYOinuRFJHXwnX_rQHaHa?pid=Api&rs=1&c=1&qlt=95&w=121&h=121", width=200)

    st.subheader("Go to Collection to see more shoes")

elif options == "collection":
    nike, adidas, nike1 = st.columns(3)

    with nike:
        st.image("black pink.jpg")
        st.image("black.jpg")

    with adidas:
        st.image("white.jpg")
        st.image("orange.jpg")

    with nike1:
        st.image("orange back.jpg")
        st.image("white nike.jpg")
    st.subheader("if you want to buy contact us using our card")

elif options == "contact":
    st.subheader("our contact number is 03336894217")
    st.subheader("[TIKTOK: follow SAA traders](https://www.tiktok.com/@saa.trades?_r=1&_t=ZS-91LDP0e5qk8)")
