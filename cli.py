#!/usr/bin/env python3
from test_demucs import DemucsPredictor

import sys

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        print("Usage: " + sys.argv[0] + " audio_file1.wav [audio_file2.wav...]");
        print("Results will be saved with appropriate filename postfixes.");
        sys.exit(1)
    demucs_predictor = DemucsPredictor()
    submission = demucs_predictor
    submission.prediction_setup()
    for fn in sys.argv[1:]:
        submission.prediction(mixture_file_path=fn,
                        bass_file_path=fn + ".bass.wav",
                        drums_file_path=fn + ".drums.wav",
                        other_file_path=fn + ".other.wav",
                        vocals_file_path=fn + ".vocals.wav",
        )
    

if __name__ == "__main__":
    main()
