from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="wLvECFL1lavclMCVrdH8W9fqI"
csecret="0mp7mp7kyuMW8NOhzbtJcclrpI91HGxwWK5pbwzV1hfh9z34PO"
atoken="1686517935139966976-ijGncht0OseemQMBzu8LTe4OpC7cPV"
asecret="jyS9UKfUhnvZKXbv0KKfpDdLkOTKogxeJxeIhM8Xy4jr8"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])