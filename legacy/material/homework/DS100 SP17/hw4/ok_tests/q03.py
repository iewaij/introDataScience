test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> connection.execute(query_q3).fetchall() ==  [('BERNIE 2016', 3),('CARSON AMERICA', 958),('CRUZ FOR PRESIDENT', 2000),('JEB 2016, INC.', 2000),('MARCO RUBIO FOR PRESIDENT', 2460),('KASICH FOR AMERICA INC', 3000),('DONALD J. TRUMP FOR PRESIDENT, INC.', 19000),('HILLARY FOR AMERICA', 61200),('4 MA PAC', None),('AAPI VICTORY FUND', None),('ABSOLUTE ENERGY PAC', None),('ACADIA HEALTHCARE COMPANY INC FEDPAC', None),('ACE CASH EXPRESS, INC. PAC', None),('ACTRIGHT', None),('ADAM SMITH FOR CONGRESS COMMITTEE', None),('ADVANCE AMERICA CASH ADVANCE CENTERS INC. PAC', None),('AES CORPORATION POLITICAL ACTION COMMITTEE; THE', None),('AFL-CIO COPE POLITICAL CONTRIBUTIONS COMMITTEE', None),('AIRCRAFT OWNERS AND PILOTS ASSOCIATION POLITICAL ACTION COMMITTEE', None),('AKIN GUMP STRAUSS HAUER & FELD LLP CIVIC ACTION COMMITTEE (AKA AGSH&F CIVIC ACTION COMMITT', None)]
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
