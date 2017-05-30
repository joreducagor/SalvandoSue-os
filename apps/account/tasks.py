from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from apps.account.models import LinkedAccount
from datetime import datetime
from textblob import TextBlob
import tweepy
 
logger = get_task_logger(__name__)

consumer_key = 'oXEsPKoCY80yfEgMqNkgbrWOh'
consumer_secret = 'qLjVnNexnKZ6ISSwUVzd9nP0l8u30EUNwi11CwWhESlBKictCf'
access_token = '850161275539771392-kfUjQUdg6TFxAUncaLeKmKwrw4gdwAL'
access_token_secret = '5OA3Dcafb5DPPpBJmHDLtN65COpUnNuAzdN92s6CpPKHQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@periodic_task(run_every = (crontab(minute = '*/10')), ignore_result = True)
def linked_accounts_analyzer():
	for linked_account in LinkedAccount.objects.all():
		users = linked_account.users.all()
		if users:
			try:
				user = api.get_user(linked_account.twitter_screen_name)
				tweets = api.user_timeline(screen_name = linked_account.twitter_screen_name, count = 20)
				results = []
				for tweet in tweets:
					results.append(tweet.text)
				if linked_account.last_tweet in results:
					index = results.index(linked_account.last_tweet)
					results = results[:index]
				if results:
					linked_account.last_tweet = results[0]
					linked_account.save()
					logger.info("Text considered dangerous")
					logger.info("--------------------------------------")
					for result in results:
						analized_text = TextBlob(str(result)).translate(to = 'en')
						if analized_text.sentiment.polarity < 0:
							logger.info(result + " ---- polarity: " + str(analized_text.sentiment.polarity))
					logger.info("--------------------------------------")

			except tweepy.TweepError as e:
				logger.info("Internal problems with the linked accounts")

	name = "linked_accounts_analyzer"