import pywhatkit
import time

# List of recipients' phone numbers and corresponding names
phone_numbers_list = [
    # Replace with original phone numbers, also don't forget to add country code eg: +911234567890
]
names_list = [
    # Corresponding names for the phone numbers
]

# Message template with placeholders for custom tags (e.g., recipient's name) you can add more placeholders 
message_template = """
    Dear {name},

    Hi, I hope you are doing well!

    This is a test message
""" 

# Specify the time to start sending messages (24-hour format) 
hour = 22
minute = 50

# Loop through the phone numbers and names to send personalized messages
for phone_number, name in zip(phone_numbers_list, names_list):
    try:
        personalized_message = message_template.format(name=name)
        
        pywhatkit.sendwhatmsg_instantly(phone_number, personalized_message)
        print(f"Message sent to {name} ({phone_number})")
        
        time.sleep(10)
    except Exception as e:
        print(f"Failed to send message to {name} ({phone_number}): {e}")
