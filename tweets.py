
import snscrape.modules.twitter as sntwitter
import pandas as pd
from sentiment_module import *
from polarity import *
query = "(to:BarackObama)"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent, getPolarity(tweet.rawContent)])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'sentiment'])

# find the most repetitive users


# assume `tweets` is a list of dictionaries containing tweet data

# create a DataFrame from the tweets data
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'sentiment'])

# find the number of tweets each user sent
user_tweet_counts = df['User'].value_counts()

# calculate the percentage of tweets replied
total_tweets = user_tweet_counts.sum()
user_tweet_percent = (user_tweet_counts / total_tweets) * 100

# create a new DataFrame with user, number of tweets, and percentage of tweets replied
user_tweet_stats = pd.DataFrame({'User': user_tweet_counts.index, 'Number of Tweets': user_tweet_counts.values, 'Percentage of Tweets Replied': user_tweet_percent.values})

# save the DataFrame to a CSV file
user_tweet_stats.to_csv('statistics.csv', index=False)



print(df)

# to save to csv
df.to_csv('tweets.csv')