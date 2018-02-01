test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> double100([3, 3, 100, 100]) == True
          True
          >>> double100([5, 2, 5, 2]) == False
          True
          >>> double100([4, 2, 4, 100, 100, 5]) == True
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
