from pytrends.request import TrendReq

def get_trending_keywords(keyword):
    """Fetch Google Trends data for a given keyword"""
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='today 3-m', geo='US', gprop='')

    data = pytrends.interest_over_time()
    if not data.empty:
        return data
    else:
        return None

# Testing
if __name__ == "__main__":
    keyword = "AI Marketing"
    print(get_trending_keywords(keyword))
