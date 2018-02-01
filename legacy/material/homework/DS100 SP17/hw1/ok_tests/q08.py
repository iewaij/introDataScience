test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(lines_to_image(test_lines), test_image)
          True

          >>> image1.shape == (240, 215, 3)
          True
          >>> image1.dtype == np.uint8
          True
          >>> np.allclose(image1[0][100], [2, 2, 3])
          True
          >>> np.allclose(image1[200][200], [8, 8, 9])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> test_lines = ['3 2\n', '0 0 0\n', '10 10 10\n', '2 2 2\n', '3 3 3\n', '4 4 4\n', '5 5 5\n']
      >>> test_image = np.array([
      ...   [ [0,0,0], [10,10,10] ],
      ...   [ [2,2,2], [3,3,3] ],
      ...   [ [4,4,4], [5,5,5] ]
      ... ])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
