import tweepy
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hashku(request):
    """


    To try it out, cut and paste the example into the form below.
    ### Example:
    > {"word1": "library", "word2": "boob"}

    Hashku searches for tweets with , mashes the tweets up, and returns a list of silly hashkus.
    By default it strips the tweets of any links. If you would like any additional customizations please let me know! [peter@peterflynn.net](mailto:peter@peterflynn.net?subject=I've got a suggestion for hashku!).
    """
    if request.method == 'POST':
        data = request.data
        word1 = data.get('word1', None)
        word2 = data.get('word2', None)

        if not (word1 and word2):
            return Response({"error": 'Please POST using word1 and word2'})

        word1 = "#" + word1
        word2 = "#" + word2
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

            word_list1 = [word for word in word_list1 if word[0:8] != 'https://' and word != "RT"]
            word_list2 = [word for word in word_list2 if word[0:8] != 'https://' and word != "RT"]

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
    else:
        return Response({"error": "You may only POST to this endpoint"})
