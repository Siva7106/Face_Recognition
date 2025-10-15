import cv2
from face_encoding import Face

# --- Setup ---
encode = Face()
encode.load_encoding_images("Images_Folder") #Change your images folder path
cap = cv2.VideoCapture(File_Path)  #Change your file path to recognize Or #Change to 0 for webcam

# --- Main Loop ---
while True:
    ret, frame = cap.read()

    # ----> ADD THIS CHECK! <----
    # If the video has ended or there's an error, ret will be False.
    # We must break the loop to avoid an error.
    if not ret:
        print("End of video or error reading frame. Exiting...")
        break

    # Your existing face detection and drawing logic
    face_area, recognize_name = encode.detect_known_faces(frame)

    for face_coordinates, name in zip(face_area, recognize_name):
        top, right, bottom, left = face_coordinates[0], face_coordinates[1], face_coordinates[2], face_coordinates[3]

        # Draw rectangle and text on the frame
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 200), 4)

    # Display the resulting frame
    cv2.imshow("Face Recognition", frame)

    # Exit loop if 'ESC' key (ASCII 27) is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# --- Cleanup ---
print("Releasing resources.")
cap.release()
cv2.destroyAllWindows()