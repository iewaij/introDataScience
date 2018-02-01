test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_output = connection.execute(query_q2).fetchall()
          >>> our_output = [('DC', 166),('CA', 64),('VA', 55),('NY', 48),('TX', 46),('FL', 43),('OH', 38),('PA', 35),('MD', 22),('IL', 18),('CO', 17),('MA', 15),('MI', 15),('AL', 14),('IN', 14),('MN', 14),('NJ', 13),('CT', 11),('GA', 11),('NC', 11),('WA', 10),('TN', 9),('AZ', 8),('LA', 8),('MO', 7),('NV', 7),('OR', 6),('WI', 6),('NM', 5),('RI', 5),('SC', 5),('AR', 4),('DE', 4),('KS', 4),('OK', 4),('WV', 4),('IA', 3),('MS', 3),('NH', 3),('VT', 3),('HI', 2),('SD', 2),('ID', 1),('ME', 1),('MT', 1),('NE', 1),('UT', 1)]
          >>> # Test that first 11 rows (ordering specified) are the same.
          >>> student_output[:11] == our_output[:11]
          True   
          >>> # Test that set of states is the same
          >>> our_states, student_states = [x[0] for x in our_output], [x[0] for x in student_output]
          >>> all([state in our_states for state in student_states]) and all([state in student_states for state in our_states])
          True
          >>> # Test that number of committees is the same
          >>> sum([x[1] for x in student_output]) == 787
          True
          >>> # Test that number of states is the same
          >>> len(student_output) == 47
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
