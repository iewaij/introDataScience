test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(derivative(np.array([0, 1, 2]), np.array([2, 4, 6])), np.array([2, 2]))
          True
          >>> np.allclose(derivative(np.arange(5), np.arange(5) ** 2), np.array([1, 3, 5, 7]))
          True
          >>> np.allclose(derivative(np.arange(5), 2 ** np.arange(5)), np.array([1, 2, 4, 8]))
          True
          
          >>> type(slopes) == np.ndarray
          True
          >>> len(slopes) == 99
          True
          >>> np.allclose(slopes[:5], np.array([ 0.9993288 ,  0.99530486,  0.98727317,  0.97526609,  0.95933195]))
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
