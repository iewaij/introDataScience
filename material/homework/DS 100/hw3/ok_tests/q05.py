test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ords = residence_areas.dropna().code.apply(lambda x: ord(x))
          >>> ranks = residence_areas.dropna().dist_rank
          >>> sum(ords - ranks) == 384
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all_ords = residence_areas.code.apply(lambda x: ord(x))
          >>> num_ords = residence_areas.dropna().code.apply(lambda x: ord(x))
          >>> sum(all_ords) - sum(num_ords) == 143
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
