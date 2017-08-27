test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_im = np.array([[ [5, 2, 2], [2, 5, 10] ] ])
          >>> np.allclose(proportion_by_channel(test_im), np.array([ 0.5, 0, 0.5 ]))
          True
          
          >>> test_im = np.array([[ [5, 2, 5], [2, 50, 50] ] ])
          >>> np.allclose(proportion_by_channel(test_im), np.array([ 0, 0, 0 ]))
          True
          
          >>> type(image_proportions) == np.ndarray
          True
          >>> len(image_proportions) == 10
          True
          >>> np.allclose(image_proportions[0], np.array([ 0.04515504,  0.01224806,  0.45127907]))
          True
          >>> np.allclose(image_proportions[9], np.array([  1.64062500e-03,   1.87500000e-04,   5.09625000e-01]))
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
