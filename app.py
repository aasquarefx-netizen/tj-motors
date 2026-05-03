import streamlit as st
from supabase import create_client

# 1. DATABASE CONNECTION
# Important: Ensure these match your Supabase Dashboard
url = 'https://hugysnyvcbachmalooma.supabase.co'
key = 'sb_publishable_uUmNjnbdtE2P3LqPWHaZag_c1xSflCY' 
supabase = create_client(url, key)

st.set_page_config(page_title="TJ Motors Showroom", page_icon="🚗")

st.title("🚗 TJ Motors Showroom")
st.write("Quality vehicles available 24/7. Click the button to chat with us!")
st.divider()

# 2. FETCH DATA FROM SUPABASE
try:
    response = supabase.table('cars').select("*").execute()
    cars = response.data
except Exception as e:
    st.error("Could not connect to the showroom database.")
    cars = []

# 3. DISPLAY CARS
if not cars:
    st.info("Our inventory is currently being updated. Please check back soon!")
else:
    for car in cars:
        with st.container():
            # Image Display logic
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
            # Your specific phone number formatted for the link
            whatsapp_number = "2348036053538"
            car_name = f"{car.get('year')} {car.get('make')} {car.get('model')}"
            message = f"Hello TJ Motors, I am interested in the {car_name} listed for ₦{price:,}."
            
            # This creates the link that opens WhatsApp
            whatsapp_link = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"
            
            st.link_button(f"💬 Inquiry about this {car.get('make')}", whatsapp_link)
            
            st.write(f"**Details:** {car.get('description')}")
            st.divider()


