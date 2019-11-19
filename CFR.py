%pylab inline
%load_ext autoreload
%autoreload 2
import numpy as np
import random

# Rock | Paper | Scissors
regretSum = np.array([0.0, 0.0, 0.0])
strategySum = np.array([0.0, 0.0, 0.0])
oppStrategy = np.array([0.4, 0.3, 0.3])

def getStrategy()
	global regretSum, strategySum
	strategy = np.maximum(regretSum, 0)
	normalizingSum = np.sum(strategy)
	if normalizingSum > 0:
		strategy /= normalizingSum
	else:
		strategy = np.ones(3)/3
	strategySum += strategy
	return strategy