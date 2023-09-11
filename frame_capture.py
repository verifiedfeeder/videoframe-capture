import argparse
import cv2
import random
import os

# Function to calculate frame brightness
def calculate_brightness(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Calculate the mean brightness value
    brightness = gray_frame.mean()
    return brightness

# Function to save a frame without timestamp
def save_frame(frame, frame_index, output_directory):
    output_file = os.path.join(output_directory, f"frame_{frame_index}.jpg")
    cv2.imwrite(output_file, frame)

def main():
    parser = argparse.ArgumentParser(description="Capture frames from a video file.")
    parser.add_argument("input_video", type=str, help="Input video file")
    parser.add_argument("--output_dir", type=str, default="captured_frames", help="Output directory for captured frames")
    parser.add_argument("--threshold", type=int, default=30, help="Minimum brightness threshold")
    parser.add_argument("--num_frames", type=int, default=10, help="Number of frames to capture")
    args = parser.parse_args()

    # Output directory to save the captured frames
    output_directory = args.output_dir
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(args.input_video)

    # Minimum brightness threshold to consider a frame as non-black/dark
    min_brightness_threshold = args.threshold

    # Number of frames to capture
    num_frames_to_capture = args.num_frames

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Generate a list of random frame indices
    random_frame_indices = random.sample(range(total_frames), num_frames_to_capture)

    # Sort the list of random frame indices to ensure frames are not consecutive
    random_frame_indices.sort()

    # List to store captured frame indices
    captured_frame_indices = []

    # Loop through the video frames
    for frame_index in random_frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()

        if not ret:
            break

        frame_brightness = calculate_brightness(frame)

        # Only save frames with brightness above the threshold
        if frame_brightness > min_brightness_threshold:
            captured_frame_indices.append(frame_index)
            save_frame(frame.copy(), frame_index, output_directory)

    # Release the video capture object
    cap.release()

    print(f"{len(captured_frame_indices)} frames captured and saved successfully in the '{output_directory}' directory.")

if __name__ == "__main__":
    main()
