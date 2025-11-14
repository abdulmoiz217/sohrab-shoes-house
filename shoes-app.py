import streamlit as st
import urllib.parse
import json
import os

# ---------- CONFIG ----------
st.set_page_config(page_title="Sohrab Shoes House", page_icon="👟", layout="wide")

TAB_HEIGHT = 30
CARD_ANIM_DURATION = "0.8s"
FEEDBACK_FILE = "feedback.json"

# ---------- Load existing feedback ----------
if os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, "r") as f:
        feedback_data = json.load(f)
else:
    feedback_data = {}

# ---------- CSS ----------
st.markdown(f"""
<style>
body {{ background: #f5f5f5; }}
.title {{ text-align: center; font-size: 40px; color: #222; font-weight: bold; }}
.subheader {{ text-align: center; color: #444; font-size: 18px; }}
.footer {{ text-align: center; color: gray; margin-top: 30px; font-size: 14px; }}
.main-container {{ max-width: 1100px; margin: 20px auto; padding: 18px; border-radius: 14px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 10px; }}
.card {{ background: #fff; border-radius: 12px; padding: 12px; transition: transform .3s ease, box-shadow .3s ease; box-shadow: 0 6px 18px rgba(17,24,39,0.04); border: 1px solid rgba(15,23,42,0.03); overflow: hidden; opacity:0; animation: fadeIn {CARD_ANIM_DURATION} forwards; }}
.card:hover {{ transform: translateY(-6px) scale(1.03); box-shadow: 0 18px 36px rgba(17,24,39,0.08); }}
.card img {{ width: 100%; border-radius: 10px; object-fit: cover; }}
.card .title {{ font-weight: 700; margin-top: 8px; color: #111827; }}
.card .meta {{ color: #6b7280; font-size: 14px; margin: 6px 0 10px; }}
.cta {{ display: inline-block; padding: 9px 14px; border-radius: 10px; background: linear-gradient(90deg, #36d1dc 0%, #5b86e5 100%); color: white !important; font-weight: 700; text-decoration: none; transition: transform .12s ease, box-shadow .12s ease; box-shadow: 0 8px 18px rgba(59,130,246,0.18); }}
.cta:hover {{ transform: translateY(-3px); box-shadow: 0 18px 36px rgba(59,130,246,0.18); }}
.stTabs {{ width: 100% !important; }}
.stTabs [role="tablist"] {{ display: flex !important; justify-content: space-around !important; width: 100% !important; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; }}
.stTabs [role="tab"] {{ flex: 1 !important; font-size: 20px !important; padding: {TAB_HEIGHT}px 0px !important; font-weight: 700 !important; text-align: center !important; margin: 0px !important; color: #444 !important; border-radius: 0px !important; transition: all 0.3s ease-in-out !important; }}
.stTabs [role="tab"]:hover {{ background-color: #d0e7ff !important; color: #0d3b66 !important; cursor: pointer; }}
.stTabs [aria-selected="true"] {{ color: white !important; background: linear-gradient(90deg, #36d1dc, #5b86e5) !important; }}
.floating-wa {{ position: fixed; bottom: 20px; right: 20px; z-index: 100; }}
@keyframes fadeIn {{ to {{ opacity: 1; }} }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ---------- PAGE TITLE ----------
st.markdown('<div class="title">Sohrab Shoes House</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Find your best shoes in wholesale at reasonable prices 👟</div>', unsafe_allow_html=True)
st.image("sohrab godam card.jpg", use_container_width=True)

# ---------- SIDEBAR ----------
st.sidebar.title("🛍️ Sohrab Shoes House")
st.sidebar.info("Filter & select options below 👇")
quantity = st.sidebar.slider("Number of pieces", 50, 10000, 50, 50)
currency = st.sidebar.selectbox("Currency", ["PKR", "USD", "EUR"])
brand_filter = st.sidebar.multiselect("Brand", ["All", "Nike", "Adidas"], default="All")

RATES = {"PKR": 1, "USD": 0.0055, "EUR": 0.0050}
CUR_SYMBOL = {"PKR": "PKR", "USD": "$", "EUR": "€"}
PRICE_PKR = 2000
PHONE = "923336894217"

def wa_link_with_message(phone: str, message: str):
    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded}"

# ---------- Render Card with Live Feedback ----------
def render_card(shoe_name, desc, img_path, brand):
    if brand_filter != ["All"] and brand not in brand_filter:
        return
    price = round(PRICE_PKR * RATES[currency], 2)
    total = round(price * quantity, 2)
    cur_sym = CUR_SYMBOL[currency]
    msg = f"Hello Sohrab Shoes, I want {quantity} pieces of {shoe_name} at {cur_sym}{price} each (Total: {cur_sym}{total})."

    st.markdown(f"""
    <div class="card">
        <img src="{img_path}" alt="{shoe_name}">
        <div class="title">{shoe_name}</div>
        <div class="meta">{desc} — {cur_sym}{price} per piece</div>
        <a class="cta" href="{wa_link_with_message(PHONE,msg)}" target="_blank">📦 Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

    # User feedback form
    with st.expander("Leave Your Feedback"):
        with st.form(f"feedback_form_{shoe_name}"):
            rating = st.slider("Rate this shoe", 1, 5, 5, key=f"rate_{shoe_name}")
            comment = st.text_area("Write your feedback", key=f"comment_{shoe_name}")
            submitted = st.form_submit_button("Submit Feedback")
            if submitted:
                if shoe_name not in feedback_data:
                    feedback_data[shoe_name] = []
                feedback_data[shoe_name].append({"rating": rating, "comment": comment})
                with open(FEEDBACK_FILE, "w") as f:
                    json.dump(feedback_data, f, indent=2)
                st.success("Thank you for your feedback!")

    # Display feedback
    if shoe_name in feedback_data:
        for fb in feedback_data[shoe_name]:
            st.markdown(f"**Rating:** {fb['rating']} ⭐  |  **Comment:** {fb['comment']}")
    else:
        st.info("No feedback yet. Be the first to comment!")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["🏠 Home", "🥿 Collection", "📞 Contact"])

with tab1:
    st.header("🏠 Welcome to Sohrab Shoes House")
    col1, col2 = st.columns(2)
    with col1:
        render_card("Nike Air Max", "Comfort + style", st.image("white nike.jpg"), "Nike")
        render_card("Nike Runner Pro", "Lightweight running shoes", st.image("white.jpg"), "Nike")
    with col2:
        render_card("Adidas Classic", "Reliable & classy", st.image("black pink.jpg"), "Adidas")
        render_card("Adidas Sport 360", "Sporty & durable", st.image("black.jpg"), "Adidas")

with tab2:
    st.header("🥿 Shoe Collection Gallery")
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        render_card("Black Pink Edition", "Limited edition 40-44", st.image("black pink.jpg"), "Adidas")
        render_card("Classic Black", "Everyday bestseller", st.image("black.jpg"), "Adidas")
    with col2:
        render_card("Pure White", "Minimal clean look", st.image("white.jpg"), "Nike")
        render_card("Orange Glow", "Bold & bright", st.image("orange.jpg"), "Nike")
    with col3:
        render_card("Orange Back Design", "Sporty panel", st.image("orange back.jpg"), "Nike")
        render_card("White Nike Runner", "Lightweight & comfy", st.image("white nike.jpg"), "Nike")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("---")
    st.header("📞 Contact Us")
    st.markdown("**Phone:** +92 333 6894217")
    st.markdown(f"[Start WhatsApp Chat]({wa_link_with_message(PHONE,'Hello, I want info about your shoes.')})")
    st.markdown("[🎵 TikTok: @saa.trades](https://www.tiktok.com/@saa.trades)", unsafe_allow_html=True)
    st.success("Thank you for visiting Sohrab Shoes House! Stay stylish 👞")

# Floating WhatsApp
st.markdown(f"""
<a href="{wa_link_with_message(PHONE,'Hello, I want info about your shoes.')}" target="_blank" class="floating-wa">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="60px">
</a>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div class="footer">© 2025 Sohrab Shoes House | Made with ❤️ in Pakistan</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
