import pandas as pd
import matplotlib.pyplot as plt
import mne
import os
import numpy as np
from matplotlib.colors import Normalize

def graph_electrodes(csv_path, time_window, electrodes):
    # Load the CSV data
    data = pd.read_csv(csv_path)

    # Define the time points (rows) from -100 to 900 ms, assuming they match the number of rows in the data
    time_points = np.linspace(time_window[0], time_window[1], len(data))

    # Plot each electrode's data
    plt.figure(figsize=(12, 8))
    for column in data.columns:
        if column in electrodes:
            plt.plot(time_points, data[column], label=column)

    plt.xlim(time_window[0], time_window[1])

    # Add labels and legend
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (µV)")
    plt.title("Voltage Measurements Across Electrodes Over Time")
    plt.legend(title="Electrode", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    # Show the plot
    plt.show()

csv_path = r"data\lawyer_spanish-english_translation_14.csv"
electrodes_all = {"Fp1","Fpz","Fp2","F7","F3","Fz","F4","F8","FC5","FC1","FC2","FC6","T7","C3","Cz","C4","T8","CP5","CP1","CP2","CP6","P7","P3","Pz","P4","P8","POz","O1","Oz","O2"}
time_window = [-100, 900]

#Afz is ground
electrodes_test = {"Fz", "Cz"}


graph_electrodes(csv_path, time_window, electrodes_test)