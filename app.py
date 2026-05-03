import streamlit as st
from supabase import create_client

# 1. DATABASE CONNECTION
# Ensure these match your Supabase Dashboard exactly
url = 'https://hugysnyvcbachmalooma.supabase.co'
key = 'sb_publishable_uUmNjnbdtE2P3LqPWHaZag_c1xSflCY' 
supabase = create_client(url, key)

# 2. PAGE SETUP
st.set_page_config(page_title="TJ Motors Showroom", page_icon="🚗", layout="centered")

# 3. HIDE FORK, GITHUB ICONS, AND STREAMLIT MENU
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    /* This makes the background look professional */
    .main { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 TJ Motors Showroom")
st.write("Quality vehicles available 24/7. Click below to chat with us on WhatsApp!")
st.divider()

# 4. FETCH DATA FROM SUPABASE
try:
    response = supabase.table('cars').select("*").execute()
    cars = response.data
except Exception as e:
    st.error("Could not connect to the database.")
    cars = []

# 5. DISPLAY CARS
if not cars:
    st.info("Our inventory is currently being updated. Please check back soon!")
else:
    for car in cars:
        with st.container():
            # IMAGE DISPLAY
            image_url = car.get('image_url')
            if image_url:
                st.image(image_url, use_container_width=True)
            else:
                st.info("📷 Photo coming soon")

            # VEHICLE INFO
            st.header(f"{car.get('year')} {car.get('make')} {car.get('model')}")
            
            price = car.get('price', 0)
            try:
                formatted_price = f"{int(price):,}"
            except:
                formatted_price = price
                
            st.subheader(f"Price: ₦{formatted_price}")
            
            # --- WHATSAPP INQUIRY BUTTON ---
            whatsapp_number = "2348036053538"
            car_name = f"{car.get('year')} {car.get('make')} {car.get('model')}"
            message = f"Hello TJ Motors, I am interested in the {car_name} listed for ₦{formatted_price}."
            
            # Create the WhatsApp link
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"
            
            st.link_button(f"💬 Inquiry about this {car.get('make')}", whatsapp_link)
            
            # DESCRIPTION
            st.write(f"**Details:** {car.get('description', 'Contact us for more details.')}")
            st.divider()


