# Fork of [richzhang/colorization](https://github.com/richzhang/colorization)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/colorization/releases). (🔥)
* Model conversion to ONNX format using the [export.py](export.py) file. (🔥)
* Installation with updated [requirements.txt](requirements.txt) file.
* Additional command line options for specifying model weights in the [demo_release.py](demo_release.py) file.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name                     | Model Size (MB) | Link                                                                                                                                                                                                             | SHA-256                                                                                                                              |
|--------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Colorization ECCV 16     | 123.0<br>123.0  | [PyTorch](https://github.com/clibdev/colorization/releases/latest/download/colorization-eccv-16.pth), [ONNX](https://github.com/clibdev/colorization/releases/latest/download/colorization-eccv-16.onnx)         | 9b330a0bae53f4ded77b1e23defbf78beaa09c10ebc4c4999e8e4f4a160b93f9<br>b4a4cecae9e84e776d665e85774815b0bb43de382813b02fb13144f8fd5d6c83 |
| Colorization SIGGRAPH 17 | 130.5<br>129.9  | [PyTorch](https://github.com/clibdev/colorization/releases/latest/download/colorization-siggraph-17.pth), [ONNX](https://github.com/clibdev/colorization/releases/latest/download/colorization-siggraph-17.onnx) | df00044c0a4d7c3edcecf6f75437ce346a66e7a42612d9b968e1a7e17dbc6f66<br>7db825910668ee321327d2e6b446e57cbc9c066e196e8be0e152bf76e1206eb7 |

# Inference

```shell
python demo_release.py --eccv16_weights colorization-eccv-16.pth --siggraph17_weights colorization-siggraph-17.pth -i imgs/ansel_adams3.jpg
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --weights colorization-eccv-16.pth --net_type eccv16
python export.py --weights colorization-siggraph-17.pth --net_type siggraph17
```
