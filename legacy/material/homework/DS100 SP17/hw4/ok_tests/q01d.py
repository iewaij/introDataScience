test = {
  'name': 'Question 1d',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_output = connection.execute(query_q1d).fetchall() 
          >>> our_output = [('C00492785', 'C00574624', 250012),('C00570739', 'C00574624', 30619),('C00283523', 'C00574624', 20000),('C00193631', 'C00458844', 17500),('C00202861', 'C00580100', 15000),('C00051979', 'C00581876', 15000),('C00197863', 'C00575795', 15000),('C00374058', 'C00580100', 14909),('C00296657', 'C00581876', 12400),('C00253153', 'C00458844', 10000),('C00204180', 'C00575795', 10000),('C00027342', 'C00575795', 10000),('C00431072', 'C00575795', 10000),('C00219642', 'C00575795', 10000),('C00034488', 'C00575795', 10000),('C00342048', 'C00575795', 10000),('C00065219', 'C00575795', 10000),('C00362384', 'C00575795', 10000),('C00385534', 'C00575795', 10000),('C00439992', 'C00575795', 10000)]
          >>> # Test that first 9 rows (all transactions above $10000) are the same.
          >>> all([i in our_output[:9] for i in student_output[:9]]) and all([i in student_output[:9] for i in our_output[:9]])
          True
          >>> # Test that output has 20 rows
          >>> len(student_output) == 20
          True
          >>> # Test that sum of transactions is the same
          >>> sum([x[2] for x in student_output]) == 500440
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