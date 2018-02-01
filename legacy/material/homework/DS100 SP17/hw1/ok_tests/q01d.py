test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> median([5, 4, 3, 2, 1]) == 3
          True
          >>> median([ 40, 30, 10, 20 ]) == 25
          True
          >>> median([ 3, 1 ]) == 2
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
