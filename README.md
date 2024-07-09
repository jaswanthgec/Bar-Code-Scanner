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
1. first of all you need to install Streamlit and other required libraries:
   ```sh
   pip install streamlit opencv-python pyzbar pandas pillow speechrecognition pyttsx3 openpyxl requests 
   ```

# Applications:

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
