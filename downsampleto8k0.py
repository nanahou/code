#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/1/18 9:07 PM
# @Author  : HOU NANA
# @Site    : http://github.com/nanahou
# @File    : downsampleto8k0.py

from scipy import signal
import os
from audioread import audioread
data_root = '/home/hounana/pytorch/enhancement/process16kto8k/wsj4bwe'
wav_list = [x for x in os.listdir(data_root) if x.endswith(".wav")]
fs_new = 8000
for wav in wav_list:
    rate_old, sig = audioread(wav)
    if cmp(rate_old, 16000):
        wav_8k = signal.resample(sig, fs_new)








# clear;
# lib_dir = '/home/hounana/matlabCode/mySignalGraph';
# path(path, lib_dir);
#
# path(path, genpath([lib_dir '/utils']));
# path(path, genpath([lib_dir '/graph']));
# path(path, genpath([lib_dir '/signal']));
# path(path, genpath([lib_dir '/prototypes']));
# path(path, genpath([lib_dir '/tools']));
#
# rec_root_c = '/home/hounana/data/wsj_VAD_add60s_beeps_2s_byWT_align/clean';
# rec_list_c = findFiles(rec_root_c, 'wav');
# fs_new = 8000;
#
# for i = 1:length(rec_list_c)
#
# words = ExtractWordsFromString_v2(rec_list_c
# {i}, '/');
# words = char(words(6));
# wav_path_c = char(rec_list_c(i));
# [wav_c, fs_c] = audioread(wav_path_c);
# wav_c = wav_c / max(abs(wav_c));
# if fs_c == 16000
#     wav_c = resample(wav_c, fs_new, fs_c);
#     rec_name_8k = ['/home/hounana/data/wsj_VAD_add60s_beeps_2s_byWT_align/clean8k/' words];
#     audiowrite(rec_name_8k, 0.75 * wav_c, fs_new);
# else
#     fprint('Wrong!');
# end
#
# end