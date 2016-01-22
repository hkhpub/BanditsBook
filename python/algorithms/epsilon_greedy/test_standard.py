execfile("core.py")

import random

random.seed(random.random())
means = [0.3, -0.7, 1.5, 0.5, 1.3, -1.5, -0.1, -1, 0.9, -0.5]
n_arms = len(means)
random.shuffle(means)
# arms = map(lambda mu: BernoulliArm(mu), means)
arms = map(lambda mu, sigma: NormalArm(mu, sigma), means, [1 for i in range(10)])
print means

f = open("algorithms/epsilon_greedy/standard_results.tsv", "w")

for epsilon in [0, 0.01, 0.1]:
  algo = EpsilonGreedy(epsilon, [], [])
  algo.initialize(n_arms)
  results = test_algorithm(algo, arms, 2000, 2000)
  for i in range(len(results[0])):
      f.write(str(epsilon) + "\t")
      f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")
  print "epsilon %.2f: %s" % (epsilon, algo.values)
f.close()
