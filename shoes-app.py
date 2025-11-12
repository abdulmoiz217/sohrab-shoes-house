import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Sohrab Shoes House", page_icon="👟", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    body {
        background-color: #f5f5f5;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #222;
        font-weight: bold;
    }
    .subheader {
        text-align: center;
        color: #444;
        font-size: 18px;
    }
    .footer {
        text-align: center;
        color: gray;
        margin-top: 30px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- MAIN TITLE ----------
st.markdown('<div class="title">Sohrab Shoes House</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Find your best shoes in wholesale at reasonable prices 👟</div>', unsafe_allow_html=True)
st.image("sohrab godam card.jpg", use_container_width=True)
st.write("Contact us for more info and buy shoes below 👇")

# ---------- SIDEBAR ----------
st.sidebar.title("🛍️ Sohrab Shoes House")
st.sidebar.info("Select an option below 👇")
options = st.sidebar.radio("Navigation", ["Home", "Collection", "Contact"])

# ---------- HOME PAGE ----------
if options == "Home":
    st.header("🏠 Welcome to Sohrab Shoes House")
    st.write("We provide premium quality **Nike** and **Adidas** shoes at the most reasonable wholesale prices.")
    st.markdown("---")

    nike, adidas = st.columns(2)

    with nike:
        st.subheader("🔥 Your Dream Nike")
        st.image("https://up.yimg.com/ib/th/id/OIP.tAZtpLwas9yqBLsTpL9-5QHaEK?pid=Api&rs=1&c=1&qlt=95&w=196&h=110",
                 width=300, caption="Nike Air Max")
        st.image("https://up.yimg.com/ib/th/id/OIP.x87oBIWS3WG_v-CsfvJNeAHaFL?pid=Api&rs=1&c=1&qlt=95&w=169&h=118",
                 width=300, caption="Nike Runner Pro")

    with adidas:
        st.subheader("⚡ Your Dream Adidas")
        st.image("https://up.yimg.com/ib/th/id/OIP.EcpWVgVvTUz7bM8Ddq1xQwHaHa?pid=Api&rs=1&c=1&qlt=95&w=121&h=121",
                 width=200, caption="Adidas Classic")
        st.image("https://up.yimg.com/ib/th/id/OIP.Rgk0bUYOinuRFJHXwnX_rQHaHa?pid=Api&rs=1&c=1&qlt=95&w=121&h=121",
                 width=200, caption="Adidas Sport 360")

    st.markdown("---")
    st.success("👉 Go to the *Collection* section to see more shoes!")

# ---------- COLLECTION PAGE ----------
elif options == "Collection":
    st.header("🥿 Shoe Collection Gallery")
    st.write("Explore our top-selling designs below:")
    st.markdown("---")

    nike, adidas, nike1 = st.columns(3)

    with nike:
        st.image("black pink.jpg", caption="Black Pink Edition")
        st.image("black.jpg", caption="Classic Black")

    with adidas:
        st.image("white.jpg", caption="Pure White")
        st.image("orange.jpg", caption="Orange Glow")

    with nike1:
        st.image("orange back.jpg", caption="Orange Back Design")
        st.image("white nike.jpg", caption="White Nike Runner")

    st.markdown("---")
    st.info("If you want to buy, please contact us using our card below 👇")

# ---------- CONTACT PAGE ----------
elif options == "Contact":
    st.header("📞 Contact Us")
    st.markdown("**Phone:** 0333-6894217")
    st.markdown("[🎵 Follow us on TikTok: @saa.trades](https://www.tiktok.com/@saa.trades?_r=1&_t=ZS-91LDP0e5qk8)")
    st.success("Thank you for visiting Sohrab Shoes House! Stay stylish 👞")

    st.markdown('<div class="footer">© 2025 Sohrab Shoes House | All Rights Reserved</div>', unsafe_allow_html=True)
