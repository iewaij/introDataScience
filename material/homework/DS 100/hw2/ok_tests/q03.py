test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(extract_text(clinton_tweets[0]), str)
          True
          >>> import datetime
          >>> isinstance(extract_time(clinton_tweets[0]), datetime.datetime)
          True
          >>> isinstance(extract_source(clinton_tweets[0]), str)
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
