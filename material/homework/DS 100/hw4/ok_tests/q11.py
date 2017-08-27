test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Test some basic statistics about hillary_design
          >>> connection.execute("select COUNT(*) from hillary_design").fetchall() == [(762000,)]
          True
          >>> len(connection.execute("select COUNT(*) from hillary_design GROUP BY trial_id").fetchall()) == 500
          True
          >>> len(connection.execute("select COUNT(*) from hillary_design GROUP BY row_id").fetchall()) == 1524
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
