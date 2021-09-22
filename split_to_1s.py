#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 5/16/2019 3:34 PM
# @Author  : HOU NANA
# @Site    : http://github.com/nanahou
# @File    : split_to_1s.py


import glob
import os.path
from scripts.dataloader import load
import soundfile as sf




split = 'train'
clean_dir = '/data/disk3/hounana/Valentini-Botinhao_16k/clean_trainset_56spk_wav'
noisy_dir = '/data/disk3/hounana/Valentini-Botinhao_16k/noisy_trainset_56spk_wav'
print('Creating {} split out of data in {}'.format(split, clean_dir))

cache_dir_d = '/data/disk3/hounana/Valentini-Botinhao_1s/16k/noisy_trainset_56spk_wav/'
cache_dir_c = '/data/disk3/hounana/Valentini-Botinhao_1s/16k/clean_trainset_56spk_wav/'
for dir in [cache_dir_d, cache_dir_c]:
    if not os.path.exists(dir):
        os.makedirs(dir)

slice_size = 16384
data_stride = 0.5


clean_names = glob.glob(os.path.join(clean_dir, '*.wav'))
noisy_names = glob.glob(os.path.join(noisy_dir, '*.wav'))
print('Found {} clean names and {} noisy names'.format(len(clean_names), len(noisy_names)))
if len(clean_names) != len(noisy_names) or len(clean_names) == 0:
    raise ValueError('No wav data found! Check your data path please')

print('now we split ', clean_dir, 'wavs!')
for name in clean_names:
    wav, rate = load(name)
    length = len(wav)
    num_slice = int((length-slice_size) / (slice_size*data_stride) + 1)
    start = 0
    base_name = os.path.splitext(os.path.basename(name))[0]
    for i in range(num_slice):
        slice = wav[start:start+slice_size]
        start += int(slice_size/2)
        slice_name = os.path.join(os.path.dirname(cache_dir_c), base_name + '_' + str(i) + '.wav')
        sf.write(slice_name, slice, rate)



print('now we split ', noisy_dir, 'wavs!')
for name in noisy_names:
    wav, rate = load(name)
    length = len(wav)
    num_slice = int((length-slice_size) / (slice_size*data_stride) + 1)
    start = 0
    base_name = os.path.splitext(os.path.basename(name))[0]
    for i in range(num_slice):
        slice = wav[start:start+slice_size]
        start += int(slice_size/2)
        slice_name = os.path.join(os.path.dirname(cache_dir_d), base_name + '_' + str(i) + '.wav')
        sf.write(slice_name, slice, rate)




clean_slice_names = glob.glob(os.path.join(cache_dir_c, '*.wav'))
noisy_slice_names = glob.glob(os.path.join(cache_dir_d, '*.wav'))
print('Found {} clean names and {} noisy names'.format(len(clean_slice_names), len(noisy_slice_names)))