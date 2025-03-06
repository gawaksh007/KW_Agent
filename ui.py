import streamlit as st
from scraper import scrape_competitor_content
from trends import get_trending_keywords
from predictor import predict_keyword_trend

st.title("🔍 Predictive Keyword & Content Opportunity Agent")

# User Inputs
website = st.text_input("Enter your website URL:")
competitor = st.text_input("Enter competitor URL:")
keyword = st.text_input("Enter a keyword to analyze:")

if st.button("Analyze"):
    st.write("Fetching competitor keywords...")
    competitor_keywords = scrape_competitor_content(competitor)
    st.write("Competitor Keywords:", competitor_keywords)

    st.write("Fetching trending data...")
    trend_data = get_trending_keywords(keyword)
    if trend_data is not None:
        st.write(trend_data)

        st.write("Predicting future trends...")
        predicted_trends = predict_keyword_trend(trend_data)
        st.line_chart(predicted_trends.set_index("ds"))  # Display as a chart
    else:
        st.write("No trend data available for this keyword.")
