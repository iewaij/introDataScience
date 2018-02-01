test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> age_classes["age_min"][4] == age_classes["age_min"][8] - 20 == 40
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> age_classes["age_max"][6] == age_classes["age_max"][3] + 15 == 54
          True
          """,
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
