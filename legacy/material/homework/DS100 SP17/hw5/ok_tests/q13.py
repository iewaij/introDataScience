test = {
  'name': 'Question 13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> num_visits = 719
          >>> rates = list(np.arange(0, 4, .2))
          >>> quick_estimates = [simulate_censored_rate_estimate(r, num_visits) for r in rates]
          >>> # The following are statistical tests
          >>> # They should pass almost all of the time for correct code
          >>> # But if they don't - try running them again
          >>> 0.27 < np.std(quick_estimates) < 0.29
          True
          >>> 0.7 < np.mean(quick_estimates) < 0.75             
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
