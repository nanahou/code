#hou nana
#2021-04-26
import os

root = '/raid/zhz_test/DNS-align/training_set_sept12/'
# clean_path = root + 'clean/'
# noisy_path = root + 'noisy/'
noise_path = root + 'noise/'

# clean_names = [x for x in os.listdir(clean_path) if x.endswith(".wav")]

# for item in clean_names:
#     words = item.split('_fileid_')
#     new_name = 'fileid_' + words[1]
#     os.rename(clean_path+item, clean_path+new_name)

# noisy_names = [x for x in os.listdir(noisy_path) if x.endswith(".wav")]

# for item in noisy_names:
#     words = item.split('_fileid_')
#     new_name = 'fileid_' + words[1]
#     os.rename(noisy_path+item, noisy_path+new_name)

noise_names = [x for x in os.listdir(noise_path) if x.endswith(".wav")]

for item in noise_names:
    words = item.split('_fileid_')
    new_name = 'fileid_' + words[1]
    os.rename(noise_path+item, noise_path+new_name)