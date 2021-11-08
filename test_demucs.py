#!/usr/bin/env python
#
# This file uses Demucs for music source speration, trained on Musdb-HQ
# See https://github.com/facebookresearch/demucs for more information
#
# NOTE: Demucs needs the model to be submitted along with your code.
# In order to download it, simply run once locally `python test_demucs.py`
#
# Making submission using the pretrained Demucs model:
# 1. Edit the `aicrowd.json` file to set your AICrowd username.
# 2. Download the pre-trained model by running
#    #> python test_demucs.py
# 3. Add the models with git lfs
#    #> git lfs install
#    #> git add models
# 4. Submit to aicrowd following the instructions from 
#    https://github.com/AIcrowd/music-demixing-challenge-starter-kit

import time

import torch.hub
import torch
import torchaudio as ta

from demucs import pretrained
from demucs.apply import apply_model

from evaluator.music_demixing import MusicDemixingPredictor


class DemucsPredictor(MusicDemixingPredictor):
    def prediction_setup(self):
        # Load your model here and put it into `evaluation` mode
        torch.hub.set_dir('./models/')

        # Use a pre-trained model
        self.separator = pretrained.get_model(name='mdx_extra')
        self.separator.eval()

    def prediction(
        self,
        mixture_file_path,
        bass_file_path,
        drums_file_path,
        other_file_path,
        vocals_file_path,
    ):

        # Load mixture
        mix, sr = ta.load(str(mixture_file_path))
        assert sr == self.separator.samplerate
        assert mix.shape[0] == self.separator.audio_channels

        b = time.time()
        # Normalize track
        mono = mix.mean(0)
        mean = mono.mean()
        std = mono.std()
        mix = (mix - mean) / std
        # Separate
        with torch.no_grad():
            estimates = apply_model(self.separator, mix[None], overlap=0.15)[0]
        print(time.time() - b, mono.shape[-1] / sr, mix.std(), estimates.std())
        estimates = estimates * std + mean


        # Store results
        target_file_map = {
            "vocals": vocals_file_path,
            "drums": drums_file_path,
            "bass": bass_file_path,
            "other": other_file_path,
        }
        for target, path in target_file_map.items():
            idx = self.separator.sources.index(target)
            source = estimates[idx]
            mx = source.abs().max()
            if mx >= 1:
                print('clipping', target, mx, std)
            source = source.clamp(-0.99, 0.99)
            ta.save(str(path), source, sample_rate=sr)


if __name__ == "__main__":
    submission = DemucsPredictor()
    submission.run()
    print("Successfully generated predictions!")
