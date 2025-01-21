import numpy as np

# System Parameters
num_users = int(input("Enter the number of users: "))
snr_range = np.linspace(0, 30, 100)  # SNR in dB
distance_from_bs = np.random.uniform(50, 500, size=num_users)  # Distance in meters
power_alloc = np.random.dirichlet(np.ones(num_users), size=1)[0]  # Dynamic power allocation
