test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> n, keys = json_description(crawl_json)
          >>> n == 1000
          True
          >>> set(keys) == {'number of checks', 'url', 'positive checks'}
          True""",
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
