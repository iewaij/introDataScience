test = {
  'name': 'Question 15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> int(Prob_pois_half_equals_0*1e6) == 606530
          True
          >>> int(Prob_pois_half_gte_1*1e6) == 393469
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
