import streamlit as st
from scraper import scrape_competitor_content
from trends import get_trending_keywords
from predictor import predict_keyword_trend

# Set up page configuration
st.set_page_config(page_title="Predictive Keyword & Content Opportunity Agent", layout="wide")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
website = st.sidebar.text_input("Enter your website URL:", value="https://yourwebsite.com")
competitor = st.sidebar.text_input("Enter competitor URL:", value="https://competitor.com")
keyword = st.sidebar.text_input("Enter a keyword to analyze:", value="AI Marketing")
analyze_button = st.sidebar.button("Analyze Now")

# Main page title and instructions
st.title("🔍 Predictive Keyword & Content Opportunity Agent")
st.markdown("""
This tool helps you discover high-potential content opportunities by analyzing competitor data and predicting keyword trends.
- **Website URL:** Your site to compare against.
- **Competitor URL:** A competitor's site to extract keywords.
- **Keyword:** The seed keyword for trend analysis.
""")

# Check if user has clicked the button
if analyze_button:
    # Validate inputs
    if not competitor or not keyword:
        st.error("Please provide both competitor URL and keyword for analysis.")
    else:
        # Use spinners to indicate processing
        with st.spinner("Fetching competitor keywords..."):
            competitor_keywords = scrape_competitor_content(competitor)
        if competitor_keywords:
            st.subheader("Competitor Keywords")
            st.write(competitor_keywords)
        else:
            st.warning("No competitor keywords found. Check the competitor URL or the website structure.")
        
        with st.spinner("Fetching trending data..."):
            trend_data = get_trending_keywords(keyword)
        if trend_data is not None:
            st.subheader("Google Trends Data")
            st.write(trend_data)
        else:
            st.warning("No trend data available for the given keyword.")
        
        if trend_data is not None:
            with st.spinner("Predicting future trends..."):
                predicted_trends = predict_keyword_trend(trend_data)
            
            st.subheader("Predicted Keyword Trend (Next 3 Months)")
            st.line_chart(predicted_trends.set_index("ds"))
            
            st.markdown("### Insights")
            st.write("The chart above forecasts the keyword's popularity over the next 90 days. Use these insights to time your content production for maximum impact.")
        
        st.success("Analysis complete!")
