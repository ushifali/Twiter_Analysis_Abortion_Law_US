import snscrape.modules.twitter as sntwitter
import pandas as pd

query=("abortion")

tweets = []
limit = 50000
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if(len(tweets) == limit):
        break
    else:
        tweets.append([tweet.date,tweet.user.username, tweet.content,tweet.user.description, tweet.source,tweet.user.location])

df = pd.DataFrame(tweets, columns=['date', 'username', 'tweet','bio','source','location'])
df.to_csv("Data_from_snscraper")
