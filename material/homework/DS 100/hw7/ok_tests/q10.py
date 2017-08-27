test = {
  'name': 'Question 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> import pandas as pd
          >>> d = pd.read_csv('q10.csv')
          >>> len(d)
          100
          >>> np.all(np.bincount(d['Label']) == [1, 52, 47])
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
