test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> new_clinton_df = make_dataframe(clinton_tweets)
          >>> len(new_clinton_df) == len(clinton_tweets)
          True
          >>> 'text' in new_clinton_df
          True
          >>> 'created_at' in new_clinton_df
          True
          >>> 'source' in new_clinton_df
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
