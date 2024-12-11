# Task Automation Scripts

This repository contains a collection of scripts and tools to automate various day-to-day tasks, such as sending automated emails, scheduling WhatsApp messages, and more. The goal is to simplify repetitive tasks and improve productivity.

---

## Features

- **Automatic Email Sender**  
  Send emails programmatically to multiple recipients with customizable templates.
  
- **WhatsApp Message Automation**  
  Schedule and send WhatsApp messages using APIs or web automation tools.
  
- **Flexible and Modular Design**  
  Easily extend the repository to include additional automation tasks.
  
- **Scheduler Integration**  
  Use tools like `cron` or task schedulers to automate recurring tasks.

---

## Requirements

Before running the scripts, ensure you have the following installed and configured:

- **Python Libraries**  
  - `smtplib`: For sending emails programmatically.  
  - `email.mime`: To format email content, including HTML and plain text.  
  - `pywhatkit`: For automating WhatsApp messages.  

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

- **Python Version**  
  - Python 3.8 or higher is recommended.  
