import numpy as np

def sic_receiver(received_signal, power_alloc, num_users):
    decoded_signals = []
    residual_signal = received_signal
    for i in range(num_users):
        user_signal = residual_signal * np.sqrt(power_alloc[i])
        decoded_signals.append(user_signal)
        residual_signal -= user_signal  # Remove decoded signal
    return decoded_signals
