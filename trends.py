import time
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def get_trending_keywords(keyword):
    """Fetch Google Trends data for a given keyword with rate limiting handling."""
    pytrends = TrendReq(hl='en-US', tz=360)
    try:
        pytrends.build_payload([keyword], cat=0, timeframe='today 3-m', geo='US', gprop='')
        data = pytrends.interest_over_time()
        if not data.empty:
            return data
        else:
            return None
    except TooManyRequestsError:
        print("Too many requests. Waiting for 60 seconds before retrying...")
        time.sleep(60)  # wait 60 seconds
        return get_trending_keywords(keyword)  # Retry recursively

# Testing the function
if __name__ == "__main__":
    keyword = "AI Marketing"
    trend_data = get_trending_keywords(keyword)
    print(trend_data)
