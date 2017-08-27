test = {
  'name': 'Question 12',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Test for correct number of trials
          >>> trials = sorted([x[0] for x in connection.execute("select * from hillary_trials").fetchall()])
          >>> trials == list(range(1, 501))
          True
          >>> # Statistical tests - these should almost always pass
          >>> small_avg = np.mean([x[1] for x in connection.execute("select * from hillary_trials").fetchall()])
          >>> 50000 < small_avg < 70000
          True
          >>> totals_avg = np.mean([x[2] for x in connection.execute("select * from hillary_trials").fetchall()])
          >>> 200000 < totals_avg < 320000
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