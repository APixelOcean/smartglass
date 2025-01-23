import cv2
import numpy as np

def adjust_brightness_contrast(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Normalize the pixel intensity to the range 0-1
    normalized = gray / 255.0

    # Apply a transformation to brighten dark regions and darken bright regions
    transformed = 1 - (normalized - 0.5)**2 * 4  # Parabolic transformation
    transformed = np.clip(transformed, 0, 1)

    # Scale back to 0-255
    result = (transformed * 255).astype(np.uint8)

    return result

def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit.")

    while True:
        # Capture each frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Apply brightness and contrast adjustment
        adjusted_frame = adjust_brightness_contrast(frame)

        # Display the original and adjusted frames
        cv2.imshow('Original', frame)
        cv2.imshow('Adjusted', adjusted_frame)

        # Quit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
