import gdown
import zipfile
import os
from track import Track

def download():
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    url = 'https://drive.google.com/uc?id=1AnvSnGQ3oUri7yC9BotQkIaTxJoucLuu'
    output = './downloads/dataset.zip'
    gdown.download(url, output, quiet=False)

    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall('./downloads')

    os.remove(output)

def get_audio_clipping_tracks():
    
    return get_audios('clipping')

def get_audio_saturation_tracks():
    
    return get_audios('saturation')

def get_audio_noise_tracks():
    
    return get_audios('noise')

def get_audios(degradation_type):

    for root, dirs, files in os.walk('./downloads/' + degradation_type +'/'):
        for name in files:
            if not name.endswith('.wav'):
                continue
            
            trackpath = os.path.join(root, name)
            jsonpath = trackpath.replace('wav', 'json')

            yield Track(trackpath, jsonpath)
