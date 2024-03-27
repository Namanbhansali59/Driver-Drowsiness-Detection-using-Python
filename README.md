# Driver Drowsiness Detection System

This Python script utilizes OpenCV to detect faces and eyes in a live video stream from a webcam. It calculates the Eye Aspect Ratio (EAR) to detect drowsiness in the driver. When the EAR falls below a certain threshold for a specific duration, it triggers an alarm indicating that the driver is drowsy.

## Prerequisites

- Python 3.x
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)

## Setup

1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the required dependencies using pip:
    ```
    pip install opencv-python numpy
    ```

3. Download the Haar cascade XML files for face and eye detection. You can find them online or use the ones provided by OpenCV.

## Usage

1. Clone this repository or download the Python script (`drowsiness_detection.py`) and the Haar cascade XML files.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script:
    ```
    python drowsiness_detection.py
    ```

4. The webcam will start capturing video. The script will analyze each frame in real-time to detect faces and eyes. If the system detects drowsiness (based on the EAR falling below a threshold), it will trigger an alarm.

5. Press the 'q' key to quit the program and close the video feed.

## Customization

You can customize the following parameters in the script according to your requirements:

- `ear_threshold`: Adjust this value to set the threshold for detecting drowsiness based on the Eye Aspect Ratio.
- `elapsed_time`: Change the duration after which the alarm is triggered once drowsiness is detected.
- You can also modify the alarm mechanism to play a sound or display a warning message instead of just printing to the console.

## Credits

- This script is inspired by various tutorials and resources available online for face and eye detection using OpenCV.
- The Haar cascade XML files used for face and eye detection are part of the OpenCV library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
