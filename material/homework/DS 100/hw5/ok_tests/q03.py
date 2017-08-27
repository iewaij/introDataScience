test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> crawls.shape[0] == 521674
          True
          >>> crawls.updated.sum() == 182755
          True
          >>> n_pages = len(set(map(lambda x: x[0], crawls.index)))
          >>> n_checks = len(set(map(lambda x: x[1], crawls.index)))
          >>> # Note that these two could be swapped in some solutions
          >>> # That's why we just check the set
          >>> index_n = {n_pages, n_checks}
          >>> index_n == {1000, 719}
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
