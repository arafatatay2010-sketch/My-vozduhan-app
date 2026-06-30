import streamlit as st
import pandas as pd

# 1. App Title and Welcome Text
st.title("Central Asia Air Quality Dashboard 🌍")
st.write("Tracking PM2.5 levels to help our community breathe easier.")

# 2. Add an interactive slider control
pollution_level = st.slider(
    label="Move the slider to simulate changing pollution levels:",
    min_value=0,
    max_value=300,
    value=45
)

# 3. Dynamic alert banners that change color based on the slider value
if pollution_level > 150:
    st.error(f"⚠️ PM2.5 is {pollution_level} - Unhealthy! Wear a protective mask outdoors.")
elif pollution_level > 50:
    st.warning(f"⚠️ PM2.5 is {pollution_level} - Moderate pollution. Sensitive groups should stay indoors.")
else:
    st.success(f"✅ PM2.5 is {pollution_level} - Clean air! Perfect for outdoor activities.")

# 4. Create and display an interactive line graph
st.subheader("Weekly Pollution Trends (Example Data)")

weekly_data = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'PM2.5 Level': [45, 82, 160, 140, 90, 55, pollution_level]
})

st.line_chart(weekly_data.set_index('Day'))
