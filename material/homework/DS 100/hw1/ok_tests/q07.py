test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(read_file_lines('3.txt')) == 68161
          True
          >>> len(file1) == 51601
          True
          >>> len(file1[5]) == 6
          True
          >>> file1[0] == '240 215\n'
          True
          >>> file1[2017] == '2 3 3\n'
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
