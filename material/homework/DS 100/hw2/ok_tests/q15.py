test = {
  'name': 'Question 15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> original_tweet_example = '@realDonaldTrump @JRACKER33 you should run for president!'
          >>> usual_retweet_example = 'Thanks,very nice! RT @melissa7889: @realDonaldTrump @JRACKER33 you should run for president!'
          >>> trump_retweet_example = '"@melissa7889: @realDonaldTrump @JRACKER33 you should run for president!" Thanks,very nice!'
          >>> tweet_type(original_tweet_example)
          'Not a retweet'
          >>> tweet_type(usual_retweet_example)
          'Aide retweet'
          >>> tweet_type(trump_retweet_example)
          'Trump retweet'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
