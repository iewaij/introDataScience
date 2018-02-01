test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> # This is testing whether the number of points follows a Poisson distribution.
          >>> import numpy as np
          >>> import math
          >>> q11_num_simulations_0 = 1000
          >>> q11_num_bins_0 = 1000
          >>> actual_dist = np.bincount([np.random.poisson(3*17) for _ in range(q11_num_simulations_0)], minlength=q11_num_bins_0) / q11_num_simulations_0
          >>> true_poisson_dist = np.exp(-3*17)*np.array([(3*17)**k / math.factorial(k) for k in range(q11_num_bins_0)])
          >>> tvd = sum(np.abs(actual_dist - true_poisson_dist)) / 2
          >>> .02 < tvd < .16
          True""",
          'hidden': False,
          'locked': False
        },
        {  
          'code': r"""
          >>> # This is testing whether the distribution of locations is uniform.
          >>> import numpy as np
          >>> q11_num_simulations_1 = 1000
          >>> q11_num_quantiles_1 = 1000
          >>> quantiles = np.arange(1, q11_num_quantiles_1 + 1) / (q11_num_quantiles_1 + 1)
          >>> actual_points = [p for _ in range(q11_num_simulations_1) for p in sample_poisson_process(5, 23)]
          >>> actual_quantile_values = np.percentile(actual_points, quantiles*100)
          >>> true_uniform = 23 * quantiles
          >>> l1_distance = sum(np.abs(true_uniform - actual_quantile_values))
          >>> 1 < l1_distance < 90
          True
          """,
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
