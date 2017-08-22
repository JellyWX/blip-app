a = [
    [], # ignore these brackets, they're just placeholder
    [ # the first set is the set of spikes for when the platform is on the right side
      # 1 #
      [[0.5,0.5]], # every line here is a different spike layout. there is a maximum of 10 spikes (this can be changed if necessary).
      [[0.8,0.95]],
      [[0.5,0.4]],
      [[0.4,0.5]],
      [[0.3,0.3]],
      [[0.9,0.5]],
      [[0.8,0.8]],
      # 2 #
      [[0.5,0.3],[0.5,0.5]], # every list inside is the relative position of one spike.
      [[0.5,0.4],[0.5,0.45]],
      [[0.9,0.5],[0.8,0.8]],
      [[0.5,0.5],[0.8,0.8]],
      # 3 #
      [[0.5,0.3], [0.5,0.5], [0.8,0.95]],
      [[0.2,0.7], [0.5,0.5], [0.5,0.4]],
      [[0.5,0.3], [0.5,0.5], [0.25,0.3]],
      [[0.5,0.4],[0.5,0.45],[0.5,0.6]],
      # 4 #
      [[0.25,0.25], [0.75,0.75], [0.25,0.75], [0.75,0.25]],
      [[0.5,0.25], [0.5,0.3], [0.5,0.5], [0.8,0.95]],
      [[0.2,0.65], [0.5,0.5], [0.5,0.4], [0.8,0.95]],
      [[0.5, 0.25], [0.5, 0.45], [0.5, 0.65], [0.5, 0.85]],
      # 5 #
      [[0.5,0.25], [0.5,0.33], [0.25,0.5], [0.8,0.95], [0.5,0.5]],
      [[0.25,0.25], [0.75,0.75], [0.25,0.75], [0.75,0.25],[0.5,0.5]],
      # 6 #
      [[0.33,0.25], [0.33,0.5], [0.33,0.75], [0.66,0.25],[0.66,0.5],[0.66,0.75]],
      [[0.25,0.25], [0.75,0.75], [0.25,0.75], [0.75,0.25], [0.5,0.5], [0.05,0.25]],
      # 7 #
      [[0.66,0.1],[0.66,0.3],[0.66,0.5],[0.66,0.7],[0.33,0.2],[0.33,0.4],[0.33,0.6]],
      # 8 #
      [[0.5,0.27],[0.5,0.32],[0.5,0.37],[0.5,0.44] , [0.5,0.56],[0.5,0.63],[0.5,0.68],[0.5,0.73]],
      # 9 #
      [[0.2,0.2], [0.2,0.6], [0.2,0.8], [0.5,0.3], [0.5,0.5], [0.5,0.7], [0.8,0.2], [0.8,0.4], [0.8,0.6]],
      # 10 #
      [[0.55, 0.25], [0.95, 0.55], [0.75, 0.5], [0.75, 0.6], [0.1, 0.4], [0.05, 0.3], [0.7, 0.55], [0.7, 0.75], [0.05, 0.85], [0.4, 0.5]],
      [[0.5, 0.25], [0.1, 0.8], [0.2, 0.6], [0.75, 0.55], [0.2, 0.25], [0.95, 0.25], [0.5, 0.9], [0.95, 0.6], [0.5, 0.5], [0.7, 0.75]]
    ],
    [ # the second set is the set of spikes for when the platform is on the left side (-1)
      # 1 #
      [[0.5,0.75]],
      [[0.5,0.5]],
      [[0.6,0.6]],
      [[0.4,0.5]],
      [[0.4,0.3]],
      [[0.2,0.95]],
      # 2 #
      [[0.2,0.95], [0.5,0.5]],
      [[0.2,0.95], [0.9,0.5]],
      [[0.5,0.6], [0.8,0.5]],
      [[0.9,0.5], [0.9,0.4]],
      [[0.5,0.35], [0.5,0.4]],
      # 3 #
      [[0.5,0.25], [0.5,0.5], [0.5,0.75]],
      [[0.5,0.35], [0.5,0.4], [0.2,0.95]],
      [[0.35,0.2], [0.4,0.36], [0.45,0.51]],
      # 4 #
      [[0.5,0.35], [0.5,0.4], [0.2,0.95], [0.5,0.45]],
      [[0.1,0.35],[0.1,0.575],[0.9,0.575],[0.9,0.775]],
      # 5 #
      [[0.2,0.95],[0.5,0.45],[0.5,0.55],[0.95,0.5],[0.05,0.45]],
      [[0.35,0.3], [0.4,0.4], [0.45,0.5], [0.5,0.6], [0.55,0.7]],
      [[0.35,0.2], [0.4,0.37], [0.45,0.53], [0.5,0.66], [0.55,0.67]],
      # 6 #
      [[0.2,0.95],[0.5,0.45],[0.5,0.55],[0.95,0.5],[0.05,0.45],[0.95,0.6]],
      # 7 #
      [[0.25,0.2], [0.65,0.55], [0.25,0.55], [0.65,0.25], [0.5,0.4], [0.9,0.4]],
      # 8 #
      [[0.66,0.1],[0.66,0.3],[0.66,0.5],[0.66,0.7],[0.33,0.2],[0.33,0.4],[0.33,0.6],[0.33,0.8]],
      # 9 #
      [[0.4, 0.65], [0.55, 0.9], [0.45, 0.75], [0.4, 0.9], [0.5, 0.55], [0.75, 0.3], [0.25, 0.65], [0.3, 0.6], [0.15, 0.85]],
      # 10 #
      [[0.35, 0.35], [0.15, 0.8], [0.3, 0.65], [0.65, 0.35], [0.85, 0.8], [0.55, 0.8], [0.6, 0.2], [0.75, 0.6], [0.05, 0.55], [0.55, 0.95]],
      [[0.05, 0.5], [0.55, 0.75], [0.05, 0.4], [0.1, 0.3], [0.65, 0.25], [0.7, 0.35], [0.3, 0.35], [0.55, 0.3], [0.6, 0.9], [0.65, 0.35]],
      [[0.75, 0.8], [0.75, 0.2], [0.45, 0.7], [0.1, 0.65], [0.35, 0.8], [0.65, 0.55], [0.95, 0.3], [0.7, 0.85], [0.65, 0.7], [0.8, 0.25]]
    ]
  ]