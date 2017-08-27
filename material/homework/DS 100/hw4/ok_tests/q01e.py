test = {
  'name': 'Question 1e',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> student_output = connection.execute(query_q1e).fetchall() 
          >>> our_output_1 = [('TED CRUZ FOR SENATE', 'CRUZ FOR PRESIDENT', 250012),('MAKE DC LISTEN', 'CRUZ FOR PRESIDENT', 30619),('DALLAS ENTREPRENEUR POLITICAL ACTION COMMITTEE', 'CRUZ FOR PRESIDENT', 20000),('THE FARM CREDIT COUNCIL POLITICAL ACTION COMMITTEE', 'MARCO RUBIO FOR PRESIDENT', 17500),('NISOURCE INC. PAC', 'KASICH FOR AMERICA INC', 15000),('THE SENATE VICTORY FUND PAC', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 15000),('CABLEVISION SYSTEMS CORPORATION POLITICAL ACTION COMMITTEE', 'HILLARY FOR AMERICA', 15000),('A WHOLE LOT OF PEOPLE FOR GRIJALVA CONGRESSIONAL COMMITTEE', 'DONALD J. TRUMP FOR PRESIDENT, INC.', 14909),('OHIO NATIONAL FINANCIAL SERVICES POLITICAL ACTION COMMITTEE', 'KASICH FOR AMERICA INC', 12400)]
          >>> our_output_2 = [('TED CRUZ FOR SENATE', 'CRUZ FOR PRESIDENT', 250012),('MAKE DC LISTEN', 'CRUZ FOR PRESIDENT', 30619),('THE FARM CREDIT COUNCIL POLITICAL ACTION COMMITTEE', 'MARCO RUBIO FOR U.S. SENATE', 17500),('DALLAS ENTREPRENEUR POLITICAL ACTION COMMITTEE', 'CRUZ FOR PRESIDENT', 15000),('NISOURCE INC. PAC', 'KASICH FOR AMERICA', 15000),('CABLEVISION SYSTEMS CORPORATION POLITICAL ACTION COMMITTEE', 'HILLARY VICTORY FUND', 15000),('OHIO NATIONAL FINANCIAL SERVICES POLITICAL ACTION COMMITTEE', 'KASICH FOR AMERICA', 12400)]
          >>> # Test that first 9 rows (all transactions above $10000) are the same.
          >>> pos1 = all([i in our_output_1 for i in student_output[:9]]) and all([i in student_output[:9] for i in our_output_1])
          >>> pos2 = all([i in our_output_2 for i in student_output[:7]]) and all([i in student_output[:7] for i in our_output_2])
          >>> (pos1 is True) or (pos2 is True)
          True
          >>> # Test that output has 20 rows
          >>> len(student_output) == 20
          True
          >>> # Test that sum of transactions is the same
          >>> sum([x[2] for x in student_output]) == 500440 or sum([x[2] for x in student_output]) == 485531
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