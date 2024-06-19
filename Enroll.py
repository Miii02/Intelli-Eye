import cv2
import os

# Create the directory to store the images if it doesn't already exist
save_dir = "D:/Downloads/Intelli Eye System/Mugshots/processed"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set the dimensions of the captured frames
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Capture and save x images
for i in range(500):
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    # Create the filename for the saved image
    filename = f"image_{i+1:03d}.jpg"
    filepath = os.path.join(save_dir, filename)
    
    # Save the image
    cv2.imwrite(filepath, frame)
    
    # Show the image on the screen (optional)
    cv2.imshow("frame", frame)
    
    # Wait for a key press to capture the next image
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()