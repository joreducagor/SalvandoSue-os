from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from apps.account.models import LinkedAccount
import tweepy
 
logger = get_task_logger(__name__)

consumer_key = 'oXEsPKoCY80yfEgMqNkgbrWOh'
consumer_secret = 'qLjVnNexnKZ6ISSwUVzd9nP0l8u30EUNwi11CwWhESlBKictCf'
access_token = '850161275539771392-kfUjQUdg6TFxAUncaLeKmKwrw4gdwAL'
access_token_secret = '5OA3Dcafb5DPPpBJmHDLtN65COpUnNuAzdN92s6CpPKHQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
@periodic_task(run_every=(crontab(minute='*/1')), ignore_result=True)
def linked_accounts_analyzer():
  for linked_account in LinkedAccount.objects.all():
    try:
      user = api.get_user(linked_account.twitter_screen_name)
      tweets = api.user_timeline(screen_name = linked_account.twitter_screen_name, count = 50)
      
      
      results = []
      for tweet in tweets:
        results.append({"tweet": tweet.text})

      return Response(
        {
          "Getting statistics for: ": str(linked_account.twitter_screen_name),
          "Followers: ": user.followers_count,
          "Tweets: ": user.statuses_count,
          "Favorites: ": user.favourites_count,
          "Friends: ": user.friends_count,
          "tweets": results
        }
      )
    except tweepy.TweepError as e:
      return Response({"Tweepy": "User not found"})



  logger.info("Getting tweets")
  now = datetime.now()
  date_now = now.strftime("%d-%m-%Y %H:%M:%S")
  # Perform all the operations you want here
  result = 2+2
  # The name of the Task, use to find the correct TaskHistory object
  name = "linked_accounts_analyzer"
  taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
  taskhistory.history.update({date_now: result})
  taskhistory.save()
  logger.info("Task finished: result = %i" % result)