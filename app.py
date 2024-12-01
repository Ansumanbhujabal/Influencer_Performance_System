import streamlit as st
import pandas as pd

df = pd.read_excel("notebooks/Final_Influencer_Data_insights_up_dec1_t2.xlsx")
df['Influencer Pic URL'] = df['Influencer Pic URL']
df.fillna("No human in video ", inplace=True)

st.set_page_config(page_title="Influencer Performance Report", layout="wide")

header_cols = st.columns([1, 4]) 
with header_cols[0]:
    st.image(
        "influencers/detected_objects_archive/image.png",
        use_container_width=True
    )
with header_cols[1]:
    st.markdown(
        """
        <style>
        .header-title {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
            padding-top: 20px;
        }
        .header-description {
            font-size: 16px;
            color: #6c757d; /* Subtle gray text for description */
            margin-top: 5px;
            padding-bottom: 20px;
        }
        </style>
        <div>
            <div class="header-title">Influencer Performance Report</div>
            <div class="header-description">
                A comprehensive table showcasing each influencer's performance, with their pictures and video links.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---") 

st.write("### Influencer Data Table")

for index, row in df.iterrows():
    st.markdown("---")  
    cols = st.columns([1, 2, 2, 2]) 
    cols[0].write(f"**{row['Influencer Label']}**")

    if row['Influencer Pic URL'] != "No Image Available":
        try:
            cols[1].image(row['Influencer Pic URL'], caption="Influencer Pic", width=150)
        except Exception as e:
            cols[1].write("No human in video")
    else:
        cols[1].write("No Image Available")

    cols[2].write(f"**Average Performance:** {row['Average Performance']}")

    if row['Video URL'] != "No Data Available":
        cols[3].markdown(f"[Watch Video]({row['Video URL']})")
    else:
        cols[3].write("No Video URL Available")


st.markdown("---")
footer_cols = st.columns([4, 1])  
footer_cols[0].markdown(
    "Made with Data by **FuelGrowth**"
)
footer_cols[1].image(
    "influencers/detected_objects_archive/image.png",
    use_container_width=True
)
