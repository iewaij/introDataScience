test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(xs) == type(ys) == np.ndarray
          True
          >>> len(xs) == len(ys) == 100
          True
          >>> np.allclose(xs[50:55], np.array([ 3.17332591,  3.23679243,  3.30025895,  3.36372547,  3.42719199]))
          True
          >>> np.allclose(ys[50:55], np.array([-0.03172793, -0.09505604, -0.1580014 , -0.22031053, -0.28173256]))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
