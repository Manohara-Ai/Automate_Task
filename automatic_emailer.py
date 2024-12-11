import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")

# List of recipients' email addresses and corresponding names
TO = [
    # Add recipient email addresses here as strings, e.g., 'recipient1@example.com', 'recipient2@example.com'
]

NAMES = [
    # Add corresponding recipient names here as strings, e.g., 'Recipient One', 'Recipient Two'
]

# If you have spreadsheet having email address and names, you can store "TO" and "NAMES" directly from spreadsheet using pandas

# SMTP server configuration
SERVER = 'smtp.gmail.com'
PORT = 587

# Sender's email credentials
FROM = ''  # Sender's email address

# Notes for sender's email credentials:
# 1. For institution accounts: Enable "less secure app access" in your Google account settings. Use your email password for "PASS"
# 2. For personal accounts: Enable 2-factor authentication and generate an app-specific password. Use this password for "PASS".

PASS = ''  # Sender's email password or app-specific password

print('Initiating Server...')

try:
    # Initialize the SMTP server
    server = smtplib.SMTP(SERVER, PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM, PASS)

    # Loop through the recipients and send emails
    for recipient, name in zip(TO, NAMES):
        # Customize email content with the recipient's name
        # Note: the content should be html content, also you can add more custom fields apart from name if you wish
        content = f'''
        <html>
        <body>
            <p>Dear {name},</p>
            <p>I hope this email finds you well. This is a sample email content.</p>
            <p>Best regards,</p>
            <p>Your Name</p>
        </body>
        </html>
        '''

        # Create email message
        msg = MIMEMultipart()

        # Subject line of the email
        msg['Subject'] = 'Sample Email Subject'  

        msg['From'] = FROM 
        msg['To'] = recipient
        msg.attach(MIMEText(content, 'html'))

        # Send the email
        server.sendmail(FROM, recipient, msg.as_string())
        print(f'Email sent to {name} ({recipient})')

    print('All emails sent successfully.')

except Exception as e:
    print(f'An error occurred: {e}')

finally:
    server.quit()
    print('Server connection closed.')
