test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> import pandas as pd
          >>> d = pd.read_csv('q09.csv')
          >>> len(d)
          10
          >>> np.all(d.sum() == [1544, 1440, 1268])
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
