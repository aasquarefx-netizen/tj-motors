import streamlit as st
from supabase import create_client

# 1. DATABASE CONNECTION
url = 'https://hugysnyvcbachmalooma.supabase.co'
key = 'sb_publishable_uUmNjnbdtE2P3LqPWHaZag_c1xSflCY' 
supabase = create_client(url, key)

st.set_page_config(page_title="TJ Motors Showroom", page_icon="🚗")

st.title("🚗 TJ Motors Showroom")
st.write("Welcome to our 24/7 digital showroom.")
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
            # Image logic to show the car photos
            image_url = car.get('image_url')
            if image_url:
                st.image(image_url, use_container_width=True)
            else:
                st.write("📷 Photo coming soon")

            st.header(f"{car.get('year')} {car.get('make')} {car.get('model')}")
            
            # Format price with ₦ and commas
            price = car.get('price', 0)
            st.subheader(f"Price: ₦{price:,}")
            
            st.write(f"**Details:** {car.get('description')}")
            st.divider()


