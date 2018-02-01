test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> data = np.array(np.matrix("1 2; 3 4; 5 6; 7 8"))
          >>> bipoly = BiPolyTrans(3)
          >>> poly_trans = bipoly.fit_transform(data)
          >>> set(sum(poly_trans)) == {4, 16, 20, 84, 100, 120, 496, 580, 680, 800}
          True
          >>> list(sum(poly_trans.T)) == [26, 220, 774, 1880]
          True""",
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
