import streamlit as st
from supabase import create_client

# 1. DATABASE CONNECTION
url = 'https://hugysnyvcbachmalooma.supabase.co'
key = 'sb_publishable_uUmNjnbdtE2P3LqPWHaZag_c1xSflCY' 
supabase = create_client(url, key)

st.set_page_config(page_title="TJ Motors Showroom", page_icon="🚗", layout="centered")

# --- CSS TO REMOVE ALL WATERMARKS & FORK BUTTON ---
st.markdown("""
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 TJ Motors Showroom")
st.write("Quality vehicles available 24/7.")
st.divider()

# 2. FETCH DATA
try:
    response = supabase.table('cars').select("*").execute()
    cars = response.data
except Exception as e:
    st.error("Connection error.")
    cars = []

# 3. DISPLAY CARS
if not cars:
    st.info("Our inventory is currently being updated.")
else:
    for car in cars:
        with st.container():
            # MULTIPLE IMAGE GALLERY LOGIC
            # It looks for the list of images first
            gallery = car.get('image_urls', [])
            main_img = car.get('image_url')

            if gallery and len(gallery) > 0:
                # This displays all images in the list
                st.image(gallery, use_container_width=True)
            elif main_img:
                st.image(main_img, use_container_width=True)
            
            st.header(f"{car.get('year')} {car.get('make')} {car.get('model')}")
            
            price = car.get('price', 0)
            st.subheader(f"Price: ₦{price:,}")
            
            # --- WHATSAPP INQUIRY ---
            whatsapp_number = "2348036053538"
            car_info = f"{car.get('year')} {car.get('make')} {car.get('model')}"
            message = f"Hello TJ Motors, I'm interested in the {car_info}."
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"
            
            st.link_button(f"💬 Inquiry about this {car.get('make')}", whatsapp_link)
            
            st.write(f"**Details:** {car.get('description')}")
            st.divider()


