# Bar-Code-Scanner
This Streamlit app captures barcode data from a video feed, accepts text or voice input, and saves the information to a GitHub repository.

[python] Certainly! Here's a short description of the Streamlit program that scans barcodes, accepts user input (text or voice), and saves the data to Google Sheets or a GitHub repository:

### Program Description

This Streamlit application captures barcode data using OpenCV, allows users to input additional information via text or voice, and saves the collected data to either Google Sheets or a GitHub repository. The application features:

1. **Barcode Scanning**:
   - Captures video frames from a user-specified URL (e.g., a network camera).
   - Uses OpenCV and `pyzbar` to decode barcodes within the captured frames.
   - Displays the captured frame and decoded barcode data.

2. **User Input**:
   - Provides a text box for manual input.
   - Allows voice input using the `speech_recognition` library, converting speech to text.

3. **Data Saving**:
   - **Google Sheets**: Saves the barcode data, current timestamp, and user input to a Google Sheets document using the `gspread` and `oauth2client` libraries for authentication and interaction with Google Sheets.
   - **GitHub**: Saves the barcode data, current timestamp, and user input to a file in a specified GitHub repository using the `PyGithub` library for interaction with the GitHub API.

### Key Features

- **Video Capture**: Users provide a URL for video capture. The application fetches frames from this URL and decodes any barcodes present in the frames.
- **Text and Voice Input**: Users can provide additional information either by typing in a text box or by recording their voice, which is then converted to text.
- **Data Storage**: The collected data is saved along with a timestamp. Users can choose to save the data in a Google Sheet or a GitHub repository file.

### Code Structure

1. **Main Functions**:
   - `get_frame(url)`: Captures a frame from the provided video URL.
   - `save_to_google_sheets(barcode_data, user_input)`: Saves data to a Google Sheets document.
   - `save_to_github(barcode_data, user_input, repo_name, file_path, token)`: Saves data to a file in a GitHub repository.
   - `speech_to_text()`: Converts speech input to text using Google's speech recognition API.

2. **Streamlit Interface**:
   - Provides text inputs for the video URL, GitHub repository details, and Google Sheets configuration.
   - Buttons for starting the barcode scanning process, recording voice input, and submitting the data.
   - Displays the captured image and scanned barcode data.

### Example Usage

1. **Barcode Scanning**:
   - Input the video capture URL.
   - Click "Start Scanning" to capture and decode barcodes from the video feed.

2. **User Input**:
   - Enter additional information in the text box or click "Record Voice" to provide input via speech.

3. **Data Submission**:
   - For Google Sheets: Ensure Google Sheets API is set up and provide the path to the credentials JSON file.
   - For GitHub: Provide the repository name, file path, and GitHub access token.
   - Click "Submit" to save the data.

### Running the App

1. Save the code in a file named `bar1.py`.
2. Run the Streamlit app with:
   ```sh
   streamlit run bar1.py
   ```

This Streamlit application combines computer vision, natural language processing, and cloud storage integration to provide a seamless barcode scanning and data collection tool suitable for various use cases such as inventory management, attendance tracking, and more.

### Required libraries
# Run the Requirements 
1. first of all you need to install Streamlit
   ```sh
   pip install streamlit
```

2. then upgrade the streamlit
   ```sh
   pip install --upgrade streamlit click
```

3. upgrade the plotly for data operations in streamlit interface
   ```sh
   pip install --upgrade plotly streamlit
```

4. This is very important
   ```sh
   pip install opencv-python-headless pyzbar pandas openpyxl
```
