
import snscrape.modules.twitter as sntwitter
import pandas as pd
from sentiment_module import *
from polarity import *
query = "(to:sollliiiiii)"
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
user_counts = df['User'].value_counts()

# sort the tweets by the orders of the most repetitive users
df_sorted = df.sort_values('User', key=lambda x: x.map(user_counts))

# build another table that tells you how many tweets each user has
user_tweet_counts = df.groupby('User').size()


print(df)

# to save to csv
df.to_csv('tweets.csv')