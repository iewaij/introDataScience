test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> int(crawl_stats['simple mle'].mean()*1000) == 337
          True
          >>> int(crawl_stats['simple mle'].std()*1000) == 332
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
