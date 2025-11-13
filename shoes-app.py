import streamlit as st
import urllib.parse

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Sohrab Shoes House", page_icon="👟", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body { background-color: #f5f5f5; }
.title { text-align: center; font-size: 40px; color: #222; font-weight: bold; }
.subheader { text-align: center; color: #444; font-size: 18px; }
.footer { text-align: center; color: gray; margin-top: 30px; font-size: 14px; }
.main-container { max-width: 1100px; margin: 20px auto; padding: 18px; border-radius: 14px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 10px; }
.card { background: #fff; border-radius: 12px; padding: 12px; transition: transform .18s ease, box-shadow .18s ease; box-shadow: 0 6px 18px rgba(17,24,39,0.04); border: 1px solid rgba(15,23,42,0.03); overflow: hidden; }
.card:hover { transform: translateY(-6px) scale(1.01); box-shadow: 0 18px 36px rgba(17,24,39,0.08); }
.card img { width: 100%; border-radius: 10px; object-fit: cover; }
.card .title { font-weight: 700; margin-top: 8px; color: #111827; }
.card .meta { color: #6b7280; font-size: 14px; margin: 6px 0 10px; }
.cta { display: inline-block; padding: 9px 14px; border-radius: 10px; background: linear-gradient(90deg, #36d1dc 0%, #5b86e5 100%); color: white !important; font-weight: 700; text-decoration: none; transition: transform .12s ease, box-shadow .12s ease; box-shadow: 0 8px 18px rgba(59,130,246,0.18); }
.cta:hover { transform: translateY(-3px); box-shadow: 0 18px 36px rgba(59,130,246,0.18); }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ---------- HOMEPAGE TITLE & BANNER ----------
st.markdown('<div class="title">Sohrab Shoes House</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Find your best shoes in wholesale at reasonable prices 👟</div>', unsafe_allow_html=True)
st.image("sohrab godam card.jpg", use_container_width=True)

# ---------- SIDEBAR ----------
st.sidebar.title("🛍️ Sohrab Shoes House")
st.sidebar.info("Select an option below 👇")
page = st.sidebar.radio("Navigation", ["Home", "Collection", "Contact"])

# ---------- Quantity slider ----------
st.sidebar.markdown("### 🧮 Select Quantity")
quantity = st.sidebar.slider("Number of pieces", min_value=50, max_value=10000, value=50, step=50)

# ---------- Currency selector ----------
st.sidebar.markdown("### 💱 Select Currency")
currency = st.sidebar.selectbox("Currency", ["PKR", "USD", "EUR"])

# ---------- Conversion rates ----------
RATES = {"PKR": 1, "USD": 0.0055, "EUR": 0.0050}
CUR_SYMBOL = {"PKR": "PKR", "USD": "$", "EUR": "€"}
PRICE_PKR = 2000
PHONE = "923336894217"

def wa_link_with_message(phone: str, message: str):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded}"

# ---------- Render card ----------
def render_card(title, desc, img_path):
    price = round(PRICE_PKR * RATES[currency], 2)
    total = round(price * quantity, 2)
    cur_sym = CUR_SYMBOL[currency]
    msg = f"Hello Sohrab Shoes, I want {quantity} pieces of {title} at {cur_sym}{price} each (Total: {cur_sym}{total})."
    st.markdown(f"""
    <div class="card">
        <img src="{img_path}" alt="{title}">
        <div class="title">{title}</div>
        <div class="meta">{desc} — {cur_sym}{price} per piece</div>
        <a class="cta" href="{wa_link_with_message(PHONE,msg)}" target="_blank">📦 Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

# ---------- PAGE CONTENT ----------
if page == "Home":
    st.header("🏠 Welcome to Sohrab Shoes House")
    st.write("We provide premium quality **Nike** and **Adidas** shoes at the most reasonable wholesale prices.")
    col1, col2 = st.columns(2)
    with col1:
        render_card("Nike Air Max", "Comfort + style — wholesale available", st.image("white nike.jpg"))
        render_card("Nike Runner Pro", "Lightweight running shoes", st.image("white.jpg"))
    with col2:
        render_card("Adidas Classic", "Reliable and classy — bulk orders welcome", st.image("black pink.jpg"))
        render_card("Adidas Sport 360", "Sporty and comfy", st.image("black.jpg"))

elif page == "Collection":
    st.header("🥿 Shoe Collection Gallery")
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        render_card("Black Pink Edition", "Limited edition — sizes 40-44", st.image("black pink.jpg"))
        render_card("Classic Black", "Everyday classic — bulk discounts available", st.image("black.jpg"))
    with col2:

        render_card("Pure White", "Clean & minimal — great seller", st.image("white.jpg"))
        render_card("Orange Glow", "Bright & bold — limited stock", st.image("orange.jpg"))
    with col3:
        render_card("Orange Back Design", "Sporty design with orange back panel", st.image("orange back.jpg"))
        render_card("White Nike Runner", "Lightweight runner — great for gyms", st.image("white nike.jpg"))
    st.markdown('</div>', unsafe_allow_html=True)
elif page == "Contact":
    st.markdown("---")
    st.header("📞 Contact Us")
    st.markdown("**Phone:** +92 333 6894217")
    st.markdown(f"[Start WhatsApp Chat with owner]({wa_link_with_message(PHONE,'Hello Sohrab Shoes, I have a question about your shoes.')})")
    st.markdown("[🎵 TikTok: @saa.trades](https://www.tiktok.com/@saa.trades)", unsafe_allow_html=True)
    st.success("Thank you for visiting Sohrab Shoes House! Stay stylish 👞")

# ---------- EXTRA PROMO ----------
st.markdown("---")
st.image("sidebar.png", caption="click this sidebar button to see more info")
st.markdown('<div class="footer">© 2025 Sohrab Shoes House | Made with ❤️ in Pakistan</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
