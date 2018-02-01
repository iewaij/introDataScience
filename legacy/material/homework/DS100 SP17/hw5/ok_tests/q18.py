test = {
  'name': 'Question 18',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> int(modified_mle(np.arange(10), 30)*1e6) == 413562
          True
          >>> sim = lambda: simulate_change_rate_estimate(1, 24, modified_mle)
          >>> simulations = [sim() for _ in range(10000)]
          >>> 1 < np.mean(simulations) < 1.05
          True
          >>> 0.25 < np.std(simulations) < 0.3
          True
          >>> # Test that "simulate_change_rate_estimate" works with other estimators
          >>> sim2 = lambda: simulate_change_rate_estimate(1, 24, lambda x, y: sum(x)/y)
          >>> simulations2 = [sim2() for _ in range(10000)]
          >>> 7.5 < np.mean(simulations2) < 8.5
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
