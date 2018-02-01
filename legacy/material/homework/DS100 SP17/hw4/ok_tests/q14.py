test = {
  'name': 'Question 14',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Test for correct number of trials
          >>> trials = sorted([x[0] for x in connection.execute("select * from bernie_props").fetchall()])
          >>> trials == list(range(1, 501))
          True
          >>> # Statistical test - this should almost always pass
          >>> prop_avg = np.mean([x[1] for x in connection.execute("select * from bernie_props").fetchall()])
          >>> 0.56 < prop_avg < 0.80
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
