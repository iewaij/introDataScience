test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> pdf_q, obs_q = compute_q_q_pairs("http://a.hatena.ne.jp/Syako/simple") 
          >>> # Test the first component of the q_q_pairs function - the pdf
          >>> 340 < int(np.mean(pdf_q)) < 370
          True
          >>> 190 < int(np.std(pdf_q)) < 220
          True
          >>> # Test the observed values
          >>> 355 < int(np.mean(obs_q)) < 385
          True
          >>> 190 < int(np.std(obs_q)) < 220
          True
          >>> # Test their interaction
          >>> -30 < int(np.mean(pdf_q - obs_q)) < 0
          True
          >>> 20 < int(np.std(pdf_q - obs_q)) < 40
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
