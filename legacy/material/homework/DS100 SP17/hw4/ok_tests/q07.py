test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_answer = connection.execute(query_q7).fetchall()
          >>> our_answer = [('HILLARY FOR AMERICA', 262923), ('BERNIE 2016', 54622)]
          >>> # Tests that our two rows are the same (order doesn't matter)
          >>> (student_answer == our_answer) or (student_answer[::-1] == our_answer)
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
