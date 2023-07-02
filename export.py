import argparse
import os
from colorizers import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', type=str, default='./colorization_release_v2-9b330a0b.pth', help='Weights path')
    parser.add_argument('--net_type', default='eccv16', type=str, help='The network architecture: eccv16 or siggraph17')
    parser.add_argument('--device', default='cpu', type=str, help='cuda:0 or cpu')
    args = parser.parse_args()

    if not os.path.exists(args.weights):
        print('Cannot find weights: {0}'.format(args.weights))
        exit()

    if args.net_type == 'eccv16':
        colorizer = eccv16(pretrained=True, weights=args.weights)
    elif args.net_type == 'siggraph17':
        colorizer = siggraph17(pretrained=True, weights=args.weights)
    else:
        print('Unsupported network type: {0}'.format(args.net_type))
        exit()

    colorizer.eval()
    colorizer.to(args.device)

    model_path = os.path.splitext(args.weights)[0] + '.onnx'
    print(model_path)

    dummy_input = torch.randn(1, 1, 256, 256).to(args.device)
    torch.onnx.export(
        colorizer,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        opset_version=18
    )
