import numpy as np

def fading_channel(num_users, distance_from_bs, fading_type="Rayleigh"):
    path_loss_exponent = 3.5  # Urban area
    path_loss = distance_from_bs**-path_loss_exponent

    if fading_type == "Rayleigh":
        fading = np.random.rayleigh(scale=1.0, size=num_users)
    elif fading_type == "Rician":
        k_factor = 10  # Rician K-factor
        fading = np.sqrt(k_factor / (k_factor + 1)) + np.random.normal(size=num_users)
    else:
        fading = np.ones(num_users)  # No fading
    return path_loss * fading
