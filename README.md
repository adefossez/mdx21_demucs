# Submission

This is the submission for MDX 2021 Track A, for Track B go to the [track_b branch](https://github.com/adefossez/mdx21_demucs/tree/track_b).


## Submission Summary

* Submission ID: 151378
* Submitter: defossez
* Final rank: 1th place on leaderboard A
* Final scores on MDXDB21:

  | SDR_song | SDR_bass | SDR_drums | SDR_other | SDR_vocals |
  | :---:    | :---:    | :---:     | :---:     | :---:      |
  | 7.33     | 8.12     | 8.04      | 5.19      | 7.97       |

## Model Summary

This model is a combination of 4 Demucs models: 2 hybrid and 2 regular. For more details,
checkout the [Demucs Model Zoo](https://github.com/facebookresearch/demucs/blob/hybrid/docs/training.md#model-zoo).

# CLI usage

If you just want to split your audio file (e.g. like with [Spleeter](https://github.com/deezer/spleeter), but better), you can use a simpler startup script.

```
$ python3 cli.py q.wav
16.146228075027466 20.0 tensor(1.1212) tensor(0.4821)
$ ls q.wav*
q.wav  q.wav.bass.wav  q.wav.drums.wav  q.wav.other.wav  q.wav.vocals.wav
```

The script assumes the models are already downloaded.


# Reproduction

## How to reproduce the submission

Follow the instructions in [test_demucs.py](test_demucs.py).

## Reproducing training

Go checkout the [Demucs training documentation](https://github.com/adefossez/demucs/blob/rel/docs/training.md)
and the [Hybrid Demucs paper](https://arxiv.org/pdf/2111.03600.pdf).


# License

This code is released under the MIT license, see the LICENSE file for more details.
