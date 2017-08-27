test = {
  'name': 'Question 17',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> int(crawl_stats["modified mle"].mean() * 1000) == 778
          True
          >>> int(crawl_stats["modified mle"].std() * 1000) == 1280
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
