test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_answer = connection.execute(query_q8).fetchall() 
          >>> our_answer = [('C00575795', 'HILLARY FOR AMERICA', 0.229135526370839),('C00577130', 'BERNIE 2016', 0.678298121635971)]
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
