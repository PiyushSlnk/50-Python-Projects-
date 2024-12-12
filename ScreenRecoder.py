import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = pyautogui.size()

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of output file
filename = "Recording.avi"

# Specify frame rate
fps = 30.0

# Create a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create a window to display the recording
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

try:
    print("Recording started. Press 'q' to stop.")
    while True:
        # Take a screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert the frame from RGB to BGR for OpenCV compatibility
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the output file
        out.write(frame)

        # Display the recording screen
        cv2.imshow("Live", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped.")
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release the VideoWriter and destroy all OpenCV windows
    out.release()
    cv2.destroyAllWindows()
    print("Resources released and windows closed.")
