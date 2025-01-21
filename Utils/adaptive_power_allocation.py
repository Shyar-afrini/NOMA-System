import numpy as np

def adaptive_power_allocation(num_users, snr_range):
    power = np.zeros((len(snr_range), num_users))
    for i, snr in enumerate(snr_range):
        # Example: Water-filling
        power[i] = np.maximum(1 / snr - 1 / np.arange(1, num_users + 1), 0)
    return power
