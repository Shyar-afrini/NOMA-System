from math import erfc
import numpy as np
from parameters.parameters import num_users, snr_range, distance_from_bs, power_alloc

def calculate_ber_noma():
    ber_noma_user1 = np.zeros(len(snr_range))
    ber_noma_user2 = np.zeros(len(snr_range))
    
    for i, snr in enumerate(snr_range):
        # Convert SNR from dB to linear
        snr_linear = 10**(snr/10)
        
        # Calculate BER for each user based on power allocation and distance
        ber_noma_user1[i] = 0.5 * erfc(np.sqrt(power_alloc[0] * snr_linear))
        ber_noma_user2[i] = 0.5 * erfc(np.sqrt(power_alloc[1] * snr_linear))
    
    return ber_noma_user1, ber_noma_user2