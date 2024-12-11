# Task Automation Scripts

This repository contains a collection of scripts and tools to automate various day-to-day tasks, such as sending automated emails, scheduling WhatsApp messages, and more. The goal is to simplify repetitive tasks and improve productivity.

---

## Features

- **Automatic Email Sender**  
  Send emails programmatically to multiple recipients with customizable templates.
  
- **WhatsApp Message Automation**  
  Schedule and send WhatsApp messages using APIs or web automation tools.

- **WhatsApp Message Automation**  
  Schedule and send WhatsApp messages using APIs or web automation tools.

- **Event Check-in with QR Code Automation**
This feature allows you to automate event check-ins using QR codes. The system creates QR codes and also scans QR codes via webcam, decodes the data, and tracks event entries in an Excel sheet. The check-in is timestamped, and it prevents multiple check-ins for the same person.
  
- **Flexible and Modular Design**  
  Easily extend the repository to include additional automation tasks.
  
- **Scheduler Integration**  
  Use tools like `cron` or task schedulers to automate recurring tasks.

---

## Requirements

Before running the scripts, ensure you have the following installed and configured:

- **Python Libraries to Install**  
  - `pywhatkit`: For automating WhatsApp messages.
  - `pyzbar`: For decoding QR codes.
  - `opencv-python`: For webcam interaction and real-time video frame processing.
  - `pandas`: For managing the event entry data in an Excel sheet.
  - `openpyxl`: For reading and writing to `.xlsx` files.

- **Email Sender Configuration**  
  - For institutional accounts:  
    - Enable "Less Secure App Access" in your Google account settings.  
    - Use your regular email password as the value for `PASS` in the script.  
  - For personal accounts:  
    - Enable two-factor authentication (2FA) in your Google account.  
    - Generate an app-specific password and use this password for `PASS` in the script.  

- **WhatsApp Automation**  
  - Ensure WhatsApp Web is active on your device.  
  - Include phone numbers in international format with the country code (e.g., `+911234567890`).

- **Webcam Configuration**  
  - Ensure your webcam is properly connected and accessible by OpenCV for QR_Based_Task.

- **Python Version**  
  - Python 3.8 or higher is recommended.  
