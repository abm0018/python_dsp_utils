import numpy as np
import matplotlib.pyplot as plt

'''
See https://en.wikipedia.org/wiki/Goertzel_algorithm
'''

def goertzel(fs, ftarg, N, samples):
    '''
    Test script for Goertzel algorithm (used for tone detection)
    '''

    # Fixed values for algorithm
    k = int( 0.5 + (N*ftarg) / fs)
    w = 2*np.pi*k / N
    cr = np.cos(2*np.pi*k/N)
    ci = np.sin(2*np.pi*k/N)
    coeff = 2 * np.cos(w)

    rtn = []

    for i in range(0, len(samples)-N, N):
        sprev = 0
        sprev2 = 0
        for samp in samples[i:i+N]:
            s = samp + coeff * sprev - sprev2
            sprev2 = sprev
            sprev = s
        power = sprev**2 + sprev2**2 - (coeff * sprev * sprev2)
        rtn.extend( [np.sqrt(power)] * N)

    rtn.extend( [0] * (len(samples) % N))
    #plt.plot(rtn)
    #plt.show()

    return rtn


