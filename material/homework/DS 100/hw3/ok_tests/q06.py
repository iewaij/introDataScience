test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> have_same_nrows(taFeng, taFengFull)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> four_row_1 = pd.DataFrame(np.zeros((4, 5)))
          >>> four_row_2 = pd.DataFrame(np.zeros((4, 7)))
          >>> six_row_1 = pd.DataFrame(np.zeros((6, 11)))
          >>> six_row_2 = pd.DataFrame(np.zeros((6, 7)))
          >>> have_same_nrows(four_row_1, four_row_2)
          True
          >>> have_same_nrows(six_row_1, six_row_2)
          True
          >>> have_same_nrows(four_row_1, six_row_1)
          False
          >>> have_same_nrows(four_row_2, six_row_2)
          False
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
