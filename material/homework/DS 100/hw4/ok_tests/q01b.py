test = {
  'name': 'Question 1b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> donations = connection.execute(query_q1b).fetchall()
          >>> our_output = [('C00492785', 'CRUZ FOR PRESIDENT', 250012),('C00570739', 'CRUZ FOR PRESIDENT', 16978),('C00197863', 'HILLARY VICTORY FUND', 15000),('C00162339', 'ENTERPRISE RENT-A-CAR', 10000),('C00202861', 'TRUMP VICTORY', 10000),('C00374058', 'WINNING CONNECTIONS', 8384),('C00406256', 'HILLARY FOR AMERICA', 5854),('C00570739', 'CRUZ FOR PRESIDENT', 5031)]
          >>> all([line in donations for line in our_output]) and all([donation in our_output for donation in donations])
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
