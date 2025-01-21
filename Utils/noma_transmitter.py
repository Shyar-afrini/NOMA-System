import numpy as np

def noma_transmitter(data_users, power_alloc):
    superposed_signal = sum(np.sqrt(power_alloc[i]) * data_users[i] for i in range(len(data_users)))
    return superposed_signal
