# Fork of [richzhang/colorization](https://github.com/richzhang/colorization)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* Additional command line options for specifying model weights in the [demo_release.py](demo_release.py) file.

# Installation

```shell
pip install -r requirements.txt
```

# Inference

```shell
python demo_release.py --eccv16_weights colorization_release_v2-9b330a0b.pth --siggraph17_weights siggraph17-df00044c.pth -i imgs/ansel_adams3.jpg
```
