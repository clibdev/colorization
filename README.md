# Fork of [richzhang/colorization](https://github.com/richzhang/colorization)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/colorization/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* Additional command line options for specifying model weights in the [demo_release.py](demo_release.py) file.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name        | Link                                                                                                                                                                                                                             |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ECCV 16     | [PyTorch](https://github.com/clibdev/colorization/releases/latest/download/colorization_release_v2-9b330a0b.pth), [ONNX](https://github.com/clibdev/colorization/releases/latest/download/colorization_release_v2-9b330a0b.onnx) |
| SIGGRAPH 17 | [PyTorch](https://github.com/clibdev/colorization/releases/latest/download/siggraph17-df00044c.pth), [ONNX](https://github.com/clibdev/colorization/releases/latest/download/siggraph17-df00044c.onnx)                           |

# Inference

```shell
python demo_release.py --eccv16_weights colorization_release_v2-9b330a0b.pth --siggraph17_weights siggraph17-df00044c.pth -i imgs/ansel_adams3.jpg
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --weights colorization_release_v2-9b330a0b.pth --net_type eccv16
python export.py --weights siggraph17-df00044c.pth --net_type siggraph17
```
