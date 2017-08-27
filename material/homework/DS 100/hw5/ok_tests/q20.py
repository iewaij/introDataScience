test = {
  'name': 'Question 20',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> 65 < int(crawl_stats['rmse'].mean()*1000) < 70
          True
          >>> 130 < int(crawl_stats['rmse'].std()*1000) < 140
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
