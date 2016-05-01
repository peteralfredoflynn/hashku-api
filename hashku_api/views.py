import tweepy
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# def thingy(request):
#     consumer_key = '0wjaB6XoXdFcgM4mYsI2yHazY'
#     consumer_secret = 'jxojv9ewbKkdCGqZhgHDryigWfHz0bJTQsSZSfg1Dxz4OAkPgl'
#     access_token = '1695521534-Wew6PSOMWmdUjOooXHC6InSNMyHXtGWsG8mEVT6'
#     access_token_secret = '1LDv8tXHT0vTUWL15JwDb7prbw0vU2XTuVyDYr5apc22B'
#
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#
#     api = tweepy.API(auth)
#
#     searched_tweets = api.search(q='#dogs')
#
#     tweets = []
#     for tweet in searched_tweets:
#         tweets.append(tweet.text)
#
#     return render(request, 'hashku_api/testing.html', {'tweets': tweets})

@api_view(['GET', 'POST'])
def thingy(request):
    if request.method == 'POST':
        data = request.data
        word1 = data['word1']
        word2 = data['word2']
        consumer_key = '0wjaB6XoXdFcgM4mYsI2yHazY'
        consumer_secret = 'jxojv9ewbKkdCGqZhgHDryigWfHz0bJTQsSZSfg1Dxz4OAkPgl'
        access_token = '1695521534-Wew6PSOMWmdUjOooXHC6InSNMyHXtGWsG8mEVT6'
        access_token_secret = '1LDv8tXHT0vTUWL15JwDb7prbw0vU2XTuVyDYr5apc22B'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        searched_tweets = api.search(q=word1)
        second_tweets = api.search(q=word2)

        tweets = []
        for tweet in searched_tweets:
            tweets.append(tweet.text)

        tweets2 = []
        for tweet in second_tweets:
            tweets2.append(tweet.text)

        smaller_list = min(len(tweets), len(tweets2))

        tweet_number = 0
        hashkus = []
        while(tweet_number < smaller_list):
            tw1 = tweets[tweet_number]
            tw2 = tweets2[tweet_number]
            word_list1 = tw1.split()
            word_list2 = tw2.split()

            count = min(len(word_list1), len(word_list2))
            index = 0
            hashku_list = []
            while(index < count):
                if index % 2 == 0:
                    hashku_list.append(word_list1[index])
                else:
                    hashku_list.append(word_list2[index])
                index += 1

            hashku = " ".join(hashku_list)
            hashkus.append(hashku)
            tweet_number += 1

    return Response({"hashkus": hashkus})
