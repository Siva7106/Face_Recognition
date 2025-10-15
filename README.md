# Face_Recognition
# Face Recognition from existing data 🎥

A Python application that performs face detection and recognition on a pre-recorded video file (`.mp4`). This project identifies known individuals from a custom dataset of images and draws their names and bounding boxes onto the video frames.

![Example of Face Recognition in Action](https://i.imgur.com/3sFj7fG.png)

---

## 🌟 Key Features

* **Video File Processing:** Analyzes any local `.mp4` video file for face recognition.
* **Accurate Recognition:** Recognizes multiple known faces by comparing them against a pre-encoded image database.
* **Dynamic Database:** Easily add new individuals to the recognition database by simply adding their images to a folder.
* **Simple & Efficient:** Built with powerful and straightforward libraries for efficient processing.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **OpenCV:** For video file reading and image processing.
* **dlib:** Provides the core face detection and facial landmark prediction models.
* **face\_recognition:** A high-level, easy-to-use API for face recognition tasks.
* **NumPy:** For numerical operations and handling image data.

---

## ⚙️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### **Prerequisites**

* Python 3.8+
* pip (Python package installer)
* CMake (required to install `dlib`)

### **Step-by-Step Guide**

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    Create a `requirements.txt` file with the following content:
    ```
    opencv-python
    face_recognition
    numpy
    ```
    Then, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```
    > **Note:** The `face_recognition` library depends on `dlib`. Ensure you have CMake installed before running this command, as it's required to build `dlib`.

4.  **Prepare the Image Database:**
    * In the project's root directory, make sure you have a folder named `images/`.
    * Place images of the people you want to recognize inside this folder.
    * **Crucially, name each image file with the person's name** (e.g., `virat_kohli.jpg`, `sachin_tendulkar.png`).

---

## ▶️ How to Run the Application

1.  **Add Your Video:** Place the `.mp4` video file you want to process into the root directory of the project.

2.  **Update the Script:** Open your main Python script (e.g., `main.py`) and find the following line:
    ```python
    cap = cv2.VideoCapture("your_video_file.mp4")
    ```
    **Change the filename** inside the parentheses to the name of your video file.

3.  **Execute the script:** Run the main script from your terminal.
    ```bash
    python main.py
    ```

4.  A window will appear, playing the video with recognized faces labeled. Press the **`ESC`** key to stop the program at any time.

---

## 🤝 How to Contribute

Contributions are welcome! If you'd like to improve the project, please fork the repository and open a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
