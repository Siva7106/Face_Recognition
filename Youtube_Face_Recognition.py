import cv2
from face_encoding import Face
import yt_dlp  # <-- 1. IMPORT THE LIBRARY

# --- Setup ---
encode = Face()
encode.load_encoding_images("images/") # <--- Load the images to the folder to Recognise using the images 

# --- NEW CODE: Get Video Stream from YouTube ---
# Paste the YouTube Shorts URL here
youtube_url = "https://www.youtube.com/" # <--- PASTE YOUR URL Of the Youtube video or Shorts

# yt-dlp options to get the best video stream URL
ydl_opts = {'format': 'best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(youtube_url, download=False)
    # Get the URL of the video stream
    stream_url = info['url']
# --- END OF NEW CODE ---


# MODIFIED LINE: Use the stream_url from YouTube
cap = cv2.VideoCapture(stream_url) 

# --- Main Loop ---
while True:
    ret, frame = cap.read()

    # This check is crucial for streams
    if not ret:
        print("End of video stream. Exiting...")
        break

    # Your existing face detection and drawing logic
    face_area, recognize_name = encode.detect_known_faces(frame)

    for face_coordinates, name in zip(face_area, recognize_name):
        top, right, bottom, left = face_coordinates[0], face_coordinates[1], face_coordinates[2], face_coordinates[3]

        # Draw rectangle and text on the frame
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 200), 4)

    # Display the resulting frame
    cv2.imshow("YouTube Face Recognition", frame)

    # Exit loop if 'ESC' key (ASCII 27) is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# --- Cleanup ---
print("Releasing resources.")
cap.release()

cv2.destroyAllWindows()

