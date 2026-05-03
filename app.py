import streamlit as st
from supabase import create_client

# 1. DATABASE CONNECTION
# Make sure to use your actual URL and Key here
url = 'https://hugysnyvcbachmalooma.supabase.co'
key = 'sb_publishable_uUmNjnbdtE2P3LqPWHaZag_c1xSflCY' 
supabase = create_client(url, key)

# Page Setup
st.set_page_config(page_title="TJ Motors Showroom", page_icon="🚗", layout="centered")

# --- CSS TO REMOVE ALL WATERMARKS & HEADERS ---
st.markdown("""
    <style>
    /* Hides the top header bar (Fork, GitHub, etc.) */
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* Hides the Streamlit footer/watermark */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Makes the background look clean */
    .main { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 2. SHOWROOM CONTENT
st.title("🚗 TJ Motors Showroom")
st.write("Quality vehicles available 24/7.")
st.divider()

# 3. FETCH DATA FROM SUPABASE
try:
    response = supabase.table('cars').select("*").execute()
    cars = response.data
except Exception as e:
    st.error("Could not connect to database.")
    cars = []

# 4. DISPLAY CARS
if not cars:
    st.info("Our inventory is currently being updated.")
else:
    for car in cars:
        with st.container():
            # Image logic
            image_url = car.get('image_url')
            if image_url:
                st.image(image_url, use_container_width=True)
            else:
                st.write("📷 Photo coming soon")

            # Car Details
            st.header(f"{car.get('year')} {car.get('make')} {car.get('model')}")
            
            price = car.get('price', 0)
            st.subheader(f"Price: ₦{price:,}")
            
            # --- WHATSAPP INQUIRY BUTTON ---
            whatsapp_number = "2348036053538"
            car_info = f"{car.get('year')} {car.get('make')} {car.get('model')}"
            message = f"Hello TJ Motors, I am interested in the {car_info} for ₦{price:,}."
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"
            
            st.link_button(f"💬 Inquiry about this {car.get('make')}", whatsapp_link)
            
            st.write(f"**Details:** {car.get('description')}")
            st.divider()


