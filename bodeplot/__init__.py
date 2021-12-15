"""
file: __init__.py

This file contains the bode class for generating bode plots
"""

# Import modules
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Configure xorg-less matplot
matplotlib.use('Agg')


class bode:
    def __init__(self, freq, title=None, rads=False, dB=False, height=10,
                 width=8):
        """
        Initialize bode plot
        """

        # Create sub plots
        figure, axis = plt.subplots(2, 1)
        figure.set_figheight(height)
        figure.set_figwidth(width)

        # Get mag plot label
        mag_label = "Magnitude"
        if dB:
            mag_label += " [dB]"

        # Get phase plot label
        phase_label = "Phase"
        if rads:
            phase_label += " [Rad]"
        else:
            phase_label += " [Deg]"

        # Get freq label
        freq_label = "Frequency [Hz]"

        # Style mag plot
        axis[0].set_title("Magnitude")
        axis[0].set_xlabel(freq_label)
        axis[0].set_ylabel(mag_label)
        axis[0].set_xlim(freq)
        axis[0].grid(True, which='major', linewidth=0.5, ls='-', alpha=0.5)
        axis[0].grid(True, which='minor', linewidth=0.5, ls='-', alpha=0.2)

        # Set scale based on unit
        if dB:
            axis[0].semilogx()
        else:
            axis[0].loglog()

        # Style phase plot
        axis[1].set_title("Phase")
        axis[1].set_xlabel(freq_label)
        axis[1].set_ylabel(phase_label)
        axis[1].set_xlim(freq)
        axis[1].semilogx()
        axis[1].grid(True, which='major', linewidth=0.5, ls='-', alpha=0.5)
        axis[1].grid(True, which='minor', linewidth=0.5, ls='-', alpha=0.2)

        # Set phase bounds based on unit
        if rads:
            axis[1].set_ylim(-np.pi - 0.2, np.pi + 0.2)
            axis[1].set_yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
        else:
            axis[1].set_ylim(-190, 190)
            axis[1].set_yticks([-180, -90, 0, 90, 180])

        # Makes axis, mag, and phase accessible
        self.axis = axis
        self.rads = rads
        self.dB = dB

    def plot(self, freq, fr, label=None):
        """
        Plot a frequency response.
        """

        # Get phase in degrees or radians
        phase = np.angle(fr)
        if not self.rads:
            phase *= 180/np.pi

        # Get mag in log or decibels
        mag = np.abs(fr)
        if self.dB:
            mag = 20 * np.log10(mag)

        # Plot phase and mag
        self.axis[0].plot(freq, mag, label=label)
        self.axis[1].plot(freq, phase, label=label)

    def save(self, path):
        """
        Save the plot to a given path
        """

        # Create legends
        self.axis[0].legend()
        self.axis[1].legend()

        # Save plot
        plt.savefig(path)
