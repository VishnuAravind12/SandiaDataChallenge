import pandas as pd
import matplotlib.pyplot as plt
import mne
import os
import numpy as np
from matplotlib.colors import Normalize

def scalp_map(csv_path, time_window, electrodes):
    # Load the CSV data
    data = pd.read_csv(csv_path)

    # Define the time points (rows) from -100 to 900 ms
    time_points = np.linspace(-100, 900, len(data))

    # Define electrode positions using the standard 10-20 layout for a 32-channel cap
    montage = mne.channels.make_standard_montage("standard_1020")

    # Convert electrodes set to list for indexing
    electrodes = list(electrodes)

    # Select data within the specified time window (200 ms to 600 ms)
    time_window_mask = (time_points >= time_window[0]) & (time_points <= time_window[1])
    selected_data = data.loc[time_window_mask, electrodes].mean()  # Average voltage over the time window

    # Create MNE info object with the selected electrodes
    info = mne.create_info(
        ch_names=electrodes,
        sfreq=1000,  # Sampling frequency, adjust if necessary
        ch_types="eeg"
    )
    info.set_montage(montage)

    # Define normalization for the color scale
    norm = Normalize(vmin=-np.max(np.abs(selected_data.values)), vmax=np.max(np.abs(selected_data.values)))

    # Plot the scalp map
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    im, _ = mne.viz.plot_topomap(
        selected_data.values,  # Voltage values for selected electrodes
        info, 
        axes=ax,
        show=False,
        cmap="RdBu_r",
        outlines='head'
    )

    # Add color bar manually with normalization
    cbar = fig.colorbar(im, ax=ax, orientation='vertical', format="%.2f")
    cbar.set_label('Voltage (µV)')

    plt.suptitle("Scalp Map Averaged from {} ms to {} ms".format(time_window[0], time_window[1]))
    plt.show()

csv_path = r"data\lawyer_spanish-english_translation_14.csv"
electrodes_all = {"Fp1","Fpz","Fp2","F7","F3","Fz","F4","F8","FC5","FC1","FC2","FC6","T7","C3","Cz","C4","T8","CP5","CP1","CP2","CP6","P7","P3","Pz","P4","P8","POz","O1","Oz","O2"}
time_window = [-100, 900]

#Afz is ground
electrodes_Fp1 = {"Fz", "Cz"}


#graph_electrodes(csv_path, time_window, electrodes_Fp1)
scalp_map(csv_path, time_window, electrodes_all)