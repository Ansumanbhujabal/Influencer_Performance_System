import streamlit as st
import pandas as pd

# Load your Excel file or data
df = pd.read_excel("notes/Final_Influencer_Data_insights_up_dec1_t2.xlsx")

# Validate and clean the image URLs
df['Influencer Pic URL'] = df['Influencer Pic URL']
# .apply(
#     lambda url: url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/") 
#     if isinstance(url, str) and "github.com" in url else "No Image Available"
# )

# Handle NaN values in other columns
df.fillna("No human in video ", inplace=True)

# Streamlit App Layout
st.set_page_config(page_title="Influencer Performance Report", layout="wide")

# Title and Description
st.title("Influencer Performance Report")
st.write("A comprehensive table showcasing each influencer's performance, with their pictures and video links.")

# Create a dynamic table
st.write("### Influencer Data Table")

# Iterate through each row and display the influencer data
for index, row in df.iterrows():
    st.markdown("---")  # Horizontal line to separate influencers
    cols = st.columns([1, 2, 2, 2])  # Define layout columns (adjust the proportions as needed)

    # Column 1: Influencer Label
    cols[0].write(f"**{row['Influencer Label']}**")

    # Column 2: Influencer Picture
    if row['Influencer Pic URL'] != "No Image Available":
        try:
            cols[1].image(row['Influencer Pic URL'], caption="Influencer Pic", width=150)
        except Exception as e:
            cols[1].write("No human in video")
    else:
        cols[1].write("No Image Available")

    # Column 3: Average Performance
    cols[2].write(f"**Average Performance:** {row['Average Performance']}")

    # Column 4: Video URL
    if row['Video URL'] != "No Data Available":
        cols[3].markdown(f"[Watch Video]({row['Video URL']})")
    else:
        cols[3].write("No Video URL Available")

# Footer
st.markdown("---")
st.write("Generated using Streamlit")
