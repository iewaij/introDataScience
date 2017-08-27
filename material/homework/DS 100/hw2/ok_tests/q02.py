test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Either your load_keys function doesn't work,
          >>> # or your keys.json file is messed up.
          >>> keys = load_keys("keys.json")
          >>> isinstance(keys, dict)
          True
          >>> 'access_token' in keys
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import json
          >>> tweets_equal = lambda a, b: json.dumps(a._json, sort_keys=True) == json.dumps(b._json, sort_keys=True)
          >>> test_save_path = "q02_test_tmp.pkl"
          >>> save_tweets(clinton_tweets, test_save_path)
          >>> reloaded_tweets = load_tweets(test_save_path)
          >>> all([tweets_equal(original, reloaded) for original, reloaded in zip(clinton_tweets, reloaded_tweets)])
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
