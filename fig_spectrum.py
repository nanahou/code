#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/4/20 4:09 PM
# @Author  : HOU NANA
# @Site    : http://github.com/nanahou
# @File    : fig_spectrum.py

# import the pyplot and wavfile modules
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.io import wavfile

def set_style():
    #plt.style.use('classic')
    
    nice_fonts = {
            # Use LaTeX to write all text
            "font.family": "serif",
            # Use 10pt font in plots, to match 10pt font in document
            "axes.labelsize": 20,
            "font.size": 20,
            # Make the legend/label fonts a little smaller
            "legend.fontsize": 18,
            "xtick.labelsize": 18,
            "ytick.labelsize": 18,
    }
    mpl.rcParams.update(nice_fonts)


# def plot_spec():
#
#     samplingFrequency, signalData = wavfile.read('/home/hounana/pytorch/enhancement/matlab_figure/disentangled-se-icassp2021/spectrum/p232_013_noisy.wav')
#
#     plt.specgram(signalData, Fs=16000, mode='magnitude')
#
#     plt.xlabel('Time [s]')
#
#     plt.ylabel('Frequency [kHz]')
#
#     plt.savefig('/home/hounana/pytorch/enhancement/matlab_figure/samples/p360_059_hf.pdf', format='pdf', bbox_inches='tight')

def plot_spec2():

    rate1, frames1 = wavfile.read("/home/hounana/pytorch/enhancement/matlab_figure/disentangled-se-icassp2021/spectrum/p232_013_clean.wav")
    fig, ax = plt.subplots()
    pxx, freq, t, cax = ax.specgram(frames1, Fs=rate1)
    ax.axis("tight")
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Frequency [kHz]')
    scale = 1e3 
    ticks = mpl.ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale))
    ax.yaxis.set_major_formatter(ticks)
    plt.savefig('/home/hounana/pytorch/enhancement/matlab_figure/disentangled-se-icassp2021/spectrum/p232_013_clean.pdf', format='pdf', bbox_inches='tight')

   


if __name__ == "__main__":
    set_style()
    plot_spec2()