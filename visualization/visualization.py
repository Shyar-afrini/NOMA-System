import sys
import os
import numpy as np

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plotly.graph_objects as go
from parameters.parameters import num_users, distance_from_bs, power_alloc, snr_range
from Utils.calculate_ber_noma import calculate_ber_noma

# users = users[]
# power_allocation = allocatePower(user)
# power_t = transmitter power 
# received_power = received(power_t, power_allocation, users) 

try:
    # Calculate BER
    ber_noma_user1, ber_noma_user2, ber_noma_user3, ber_noma_user4 = calculate_ber_noma()
    
    # Validate BER data
    if np.any(np.isnan(ber_noma_user1)) or np.any(np.isnan(ber_noma_user2)):
        raise ValueError("BER calculations contain NaN values")
        
    # Create figure with validated data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=snr_range, y=ber_noma_user1, mode='lines', name='User 1 (NOMA)'))
    fig.add_trace(go.Scatter(x=snr_range, y=ber_noma_user2, mode='lines', name='User 2 (NOMA)'))
    
    # Enhanced layout
    fig.update_layout(
        title="BER vs. SNR for NOMA",
        xaxis_title="SNR (dB)",
        yaxis_title="BER",
        template="plotly_dark",
        yaxis_type="log",  # Log scale for BER
        showlegend=True
    )
    
    # Configure renderer
    fig.show(renderer="browser", config={'scrollZoom': True})
    
except Exception as e:
    print(f"Error generating plot: {str(e)}")