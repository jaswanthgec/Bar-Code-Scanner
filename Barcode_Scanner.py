import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import datetime
import os
from PIL import Image
import speech_recognition as sr
import requests
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import time

# Function to capture frame from URL or local file
def get_frame(source):
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        st.error("Error: Unable to open video capture.")
        return None

    ret, frame = cap.read()
    cap.release()
    if ret:
        return frame
    else:
        st.error("Error: Unable to read frame from video capture.")
        return None

# Function to save data to Excel
def save_to_excel(barcode_data, user_input, filename='scanned_barcodes.xlsx'):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_row = {'Id': barcode_data, 'Time': current_time, 'User Input': user_input}
    
    if os.path.exists(filename):
        barcode_df = pd.read_excel(filename, engine='openpyxl')
    else:
        barcode_df = pd.DataFrame(columns=['Id', 'Time', 'User Input'])

    barcode_df = pd.concat([barcode_df, pd.DataFrame([new_row])], ignore_index=True)
    barcode_df.to_excel(filename, index=False, engine='openpyxl')
    return new_row

# Function to convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.success("You said: " + text)
            return text
        except sr.UnknownValueError:
            st.error("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Function to make a GitHub API request and maintain persistent connection
def get_github_user_info():
    try:
        api_key = st.secrets["GITHUB"]["GITHUB_API_KEY"]
    except KeyError:
        st.error("GitHub API key not found. Please set the GITHUB_API_KEY secret.")
        return None

    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {api_key}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        st.success("Successfully connected to GitHub API")
        return response.json()
    else:
        st.error(f"Failed to connect to GitHub API. Status code: {response.status_code}")
        return None

# Function to speak text using gTTS and pydub
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    sound = AudioSegment.from_mp3("speech.mp3")
    play(sound)
    os.remove("speech.mp3")

# Initialize Streamlit session state
if 'barcode_data' not in st.session_state:
    st.session_state.barcode_data = ""

if 'github_user_info' not in st.session_state:
    st.session_state.github_user_info = get_github_user_info()

# Streamlit interface
st.title("Barcode Scanner")

url = st.text_input("Enter the URL for video capture or local video file path", "http://192.168.0.125:8080/video")

def scan_barcodes():
    while True:
        st.write("Trying to capture frame...")
        frame = get_frame(url)
        
        if frame is not None:
            barcodes = decode(frame)
            if barcodes:
                for barcode in barcodes:
                    st.session_state.barcode_data = barcode.data.decode('utf-8')
                    st.write(f"Barcode found: {st.session_state.barcode_data}")

                    # Display the captured frame
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    st.image(img, caption="Scanned Image")

                    # Speak prompt
                    speak("Report your query")

                    # Record voice input
                    user_input = speech_to_text()
                    if user_input:
                        new_row = save_to_excel(st.session_state.barcode_data, user_input)
                        st.success(f"Data saved: {new_row}")

                        # Speak confirmation
                        speak("Your query is reported")
                    else:
                        st.error("User input is required to save data.")
                    
                    return  # Exit the function after processing a barcode
            else:
                st.write("No barcodes found in the current frame.")
        else:
            st.write("Error capturing frame from the camera.")
        time.sleep(1)  # Add a delay to prevent excessive looping

if st.button("Start Scanning"):
    scan_barcodes()

# Voice input button
if st.button("Record Voice"):
    user_input = speech_to_text()
    if st.session_state.barcode_data and user_input:
        new_row = save_to_excel(st.session_state.barcode_data, user_input)
        st.success(f"Data saved: {new_row}")
        speak("Your query is reported")
    else:
        st.error("Barcode and user input are required to save data.")

# Admin section to view past records
st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line for separation

st.header("Admin Section")
admin_password = st.text_input("Enter admin password to view past records:", type="password", placeholder="Enter password here...")

if admin_password:
    if admin_password == "123456":  # Replace '123456' with your actual admin password
        st.write("Access granted.")
        if os.path.exists('scanned_barcodes.xlsx'):
            df = pd.read_excel('scanned_barcodes.xlsx', engine='openpyxl')
            st.write("Past Records:")
            st.dataframe(df)
    else:
        st.write("Access denied. Please enter the correct admin password.")
