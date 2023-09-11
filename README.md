# Frame Capture from Video

**Author:** Verified Feeder

**License:** [GNU General Public License v3.0 (GPL-3.0)](LICENSE)

## Description

This Python script captures frames from a video file, selecting random frames based on a brightness threshold. It provides an efficient way to extract non-dark frames from a video for various applications such as video analysis, image processing, or content summarization.

## Features

- Randomly captures frames from a video.
- Allows specifying the minimum brightness threshold.
- Supports specifying the number of frames to capture.
- Saves the captured frames to an output directory.

## Requirements

- Python 3.x
- OpenCV (cv2) library

## Usage

To use this script, follow the instructions below:

1. Ensure you have Python 3.x installed on your system.

2. Install the OpenCV library if you haven't already:

   ```bash
   pip install opencv-python
   ```

3. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/verifiedfeeder/videoframe-capture.git
   ```

4. Navigate to the project directory

5. Run the script with the following command, customizing the arguments as needed:

   ```bash
   python frame_capture.py input_video.mp4 --output_dir captured_frames --threshold 30 --num_frames 10
   ```

   - `input_video.mp4`: Replace with the path to your input video file.
   - `--output_dir`: (Optional) Specify the output directory for captured frames (default: captured_frames).
   - `--threshold`: (Optional) Set the minimum brightness threshold (default: 30).
   - `--num_frames`: (Optional) Set the number of frames to capture (default: 10).

6. The captured frames will be saved in the specified output directory.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions to this project are welcome. Feel free to open issues or submit pull requests.
