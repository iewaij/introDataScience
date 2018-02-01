test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> summer_or_winter(expanded_images[0])
          False
          >>> summer_or_winter(expanded_images[1])
          True
          >>> summer_or_winter(expanded_images[2])
          True
          >>> summer_or_winter(expanded_images[3])
          False
          >>> summer_or_winter(expanded_images[4])
          True
          >>> summer_or_winter(expanded_images[5])
          True
          >>> summer_or_winter(expanded_images[6])
          False
          >>> summer_or_winter(expanded_images[7])
          False
          >>> summer_or_winter(expanded_images[8])
          True
          >>> summer_or_winter(expanded_images[9])
          False
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
