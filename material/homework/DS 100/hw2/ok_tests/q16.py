test = {
  'name': 'Question 16',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'Aide retweet' in trump_pivoted
          True
          >>> 'Not a retweet' in trump_pivoted
          True
          >>> 'Trump retweet' in trump_pivoted
          True
          >>> "Twitter for iPhone" in trump_pivoted.index
          True
          >>> trump_total = sum(trump_pivoted['Trump retweet'])
          >>> non_retweet_total = sum(trump_pivoted['Not a retweet'])
          >>> aide_total = sum(trump_pivoted['Aide retweet'])
          >>> trump_total > 0
          True
          >>> non_retweet_total > 0
          True
          >>> aide_total > 0
          True
          >>> trump_total + non_retweet_total + aide_total == len(trump_df)
          True
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
