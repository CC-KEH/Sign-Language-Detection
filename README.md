# Sign Language Detection using YOLOv5 Model

This repository contains a program for detecting sign language gestures using the YOLOv5 object detection model. The model is trained to detect commonly used signs such as "hello", "goodbye", "please", "sorry", "thanks", "no", "yes", and "I love you".

## Getting Started

To get started with using the sign language detection program, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- PyTorch
- OpenCV
- NumPy
- Roboflow account (for dataset augmentation, if you want to train your own model) 

### Usage

1. Clone this repository:

```bash
git clone https://github.com/CC-KEH/sign-language-detection.git
```

2. Dataset Creation and Augmentation:

- Gather Images: Simply run `generate_dataset.py`, this will create a directory `CollectedImages`.

- Labeling: I used Roboflow, to annotate, augmentate and split the dataset for train,val and testing.

- Dataset Format: dataset/
                        train/
                                /images
                                /labels
                        test/   
                                /images
                                /labels
                        valid/
                                /images
                                /labels
                        data.yaml

3. Training:

- run `train.ipynb`

- I used yolov5s for training.

### Steps to run the model:

1. Go to yolov5 directory:

```bash
cd yolov5
```

3. Run the file `run.py` program:

```bash
python run.py
```

This will launch the program, and it will start detecting sign language gestures using your webcam.
If you want to change the camera, simply change the value from run.py file.

##### Note:

If you encounter an issue: **cannot instantiate 'PosixPath' on your system**

Do this:
    ```
    import pathlib
    temp = pathlib.PosixPath
    pathlib.PosixPath = pathlib.WindowsPath
    ```
    Add this In files where you find the use of torch.hub.load()
    then simply replace torch.hub.load() with patlib.PosixPath()



## Model

The YOLOv5 model used for sign language detection is trained on a custom dataset containing images of various sign language gestures. The model is fine-tuned to detect specific signs, including "please", "hello", "goodbye", "sorry", "thanks", "no", "yes", and "I love you". You can find the model weights in the `weights/` directory.

## Contributing

Contributions to improve the sign language detection program are welcome. If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of the YOLOv5 repository for their work on developing the YOLOv5 model.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx