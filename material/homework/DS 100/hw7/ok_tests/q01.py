test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> import pandas as pd
          >>> d = pd.read_csv('q01.csv')
          >>> len(d['value'])
          505
          >>> sum(d['value'])
          509040""",
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
