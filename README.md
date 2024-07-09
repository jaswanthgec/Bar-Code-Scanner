# Bar Code Scanner & Voice Recognizer
This Streamlit app captures barcode data from a video feed, accepts text or voice input, and saves the information to a GitHub repository.

[python] Certainly! Here's a short description of the Streamlit program that scans barcodes, accepts user input (text or voice), and saves the data to Google Sheets or a GitHub repository:

## Description of the Streamlit Project

### Definition
This project is a Streamlit web application that uses OpenCV (cv2) and Pyzbar to capture video frames from a specified URL, decode barcodes from these frames, convert speech to text, and save the captured data into an Excel file. The application also interacts with the GitHub API and uses text-to-speech for voice feedback.

### Uses and Applications
- **Barcode Scanning**: Capture and decode barcodes from live video feeds.
- **Speech to Text**: Convert voice input into text using Google Speech Recognition.
- **Data Storage**: Save barcode data along with user input into an Excel file.
- **Voice Feedback**: Provide voice prompts and feedback using gTTS and pydub.
- **GitHub API Interaction**: Fetch and display GitHub user information using a personal access token.

### Key Features
1. **Video Frame Capture**: Capture frames from a video URL and decode barcodes.
2. **Excel Integration**: Save decoded barcode data and user input into an Excel file.
3. **Speech Recognition**: Convert speech to text to capture user input.
4. **Voice Prompts**: Use text-to-speech to guide the user and confirm actions.
5. **Admin Section**: View past records with password-protected access.
6. **GitHub API**: Retrieve GitHub user information using a personal access token.

### Installation Procedure

#### Step 1: Install Python and Dependencies
Ensure you have Python installed on your system. Then, create a `requirements.txt` file with the following content:

```plaintext
streamlit
opencv-python
pyzbar
pandas
openpyxl
Pillow
speechrecognition
gtts
pydub
requests
```

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

#### Step 2: Install ffmpeg
Download and install ffmpeg from [FFmpeg's official website](https://ffmpeg.org/download.html). Ensure the path to `ffmpeg` executable is added to your system's PATH environment variable.

#### Step 3: Set Up Environment Variables
Set the `GITHUB_API_KEY` environment variable with your GitHub API token. For example:

- **Linux/macOS**:
  ```bash
  export GITHUB_API_KEY=your_github_api_key_here
  ```
- **Windows**:
  ```bash
  set GITHUB_API_KEY=your_github_api_key_here
  ```

#### Step 4: Run the Application
Save your script as `app.py` and run the Streamlit application:

```bash
streamlit run app.py
```

### Example Usage
1. **Start the Application**: Open your terminal and run the Streamlit app using the command above.
2. **Enter Video URL**: Provide the URL for the video stream from which barcodes will be captured.
3. **Start Scanning**: Click the "Start Scanning" button to capture frames and decode barcodes.
4. **Voice Input**: Use the voice input feature to record and save user queries along with the barcode data.
5. **View Past Records**: Admins can view past scanned records by entering the correct admin password.

### Additional Notes
- Ensure your system has an active internet connection for Google Speech Recognition and GitHub API features.
- The admin password for accessing past records should be securely managed and changed as needed.

# Potential Applications:

This code involves several key functionalities such as video capture, barcode scanning, speech recognition, and data storage. Here are some related applications that could leverage these capabilities:

### 1. Inventory Management System
**Description**: An application to manage inventory by scanning barcodes to add items, update quantities, and track inventory levels.

**Features**:
- Scan barcodes to add new items or update existing items in the inventory.
- Store item details such as name, quantity, and price in a database or Excel file.
- Generate reports on inventory levels, low stock alerts, and restocking needs.

### 2. Attendance Tracking System
**Description**: An application to track attendance by scanning barcodes or QR codes on ID cards.

**Features**:
- Scan barcodes or QR codes to log attendance for students or employees.
- Store attendance records in a database or Excel file.
- Generate attendance reports and calculate attendance percentages.

### 3. Library Management System
**Description**: An application to manage library operations by scanning barcodes on books.

**Features**:
- Scan barcodes to issue or return books.
- Maintain a database of issued books, due dates, and overdue fines.
- Generate reports on book availability and borrowing history.

### 4. Product Information System
**Description**: An application to provide product information by scanning barcodes on product packaging.

**Features**:
- Scan barcodes to fetch product details such as name, price, and description from a database or API.
- Display product information on a user interface.
- Store scanned product data for analytics and reporting.

### 5. Event Registration System
**Description**: An application to manage event registration by scanning QR codes on tickets.

**Features**:
- Scan QR codes to register attendees for an event.
- Store attendee information in a database or Excel file.
- Generate reports on attendee count, registration status, and event analytics.

### 6. Asset Tracking System
**Description**: An application to track assets by scanning barcodes or QR codes on asset tags.

**Features**:
- Scan barcodes to log asset check-ins and check-outs.
- Maintain a database of asset details, locations, and usage history.
- Generate reports on asset utilization and maintenance schedules.

### 7. Healthcare Management System
**Description**: An application to manage patient records by scanning barcodes on patient wristbands.

**Features**:
- Scan barcodes to retrieve patient information and medical history.
- Store patient visit details and treatment records in a database or Excel file.
- Generate reports on patient visits, treatments, and outcomes.

### 8. Warehouse Management System
**Description**: An application to manage warehouse operations by scanning barcodes on packages.

**Features**:
- Scan barcodes to log incoming and outgoing shipments.
- Maintain a database of package details, locations, and shipping status.
- Generate reports on warehouse inventory, shipping efficiency, and order fulfillment.

### 9. Retail Point of Sale (POS) System
**Description**: An application to manage retail sales by scanning barcodes on products at checkout.

**Features**:
- Scan barcodes to add products to the shopping cart.
- Calculate total price, apply discounts, and process payments.
- Store sales transactions in a database or Excel file for reporting.

### 10. Customer Feedback System
**Description**: An application to collect customer feedback by scanning QR codes on receipts.

**Features**:
- Scan QR codes to link to a feedback form.
- Use speech recognition to allow customers to provide feedback via voice.
- Store feedback data in a database or Excel file for analysis.
