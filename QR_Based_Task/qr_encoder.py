import os
import pandas as pd
import qrcode

# Create the directory for saving QR codes
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

# Load the spreadsheet (Replace "path_to_excel_sheet.xlsx" with the actual path)
spreadsheet = pd.read_excel("path_to_excel_sheet.xlsx")

def create_qr(row):
    '''
        Note: The column names used here are "Name", "Unique_Number", "Email_Id", "Phone_Number"
        Ensure to match cases and column names while making QR Codes
    '''
    qr_data = f"{row['Name']};{row['Unique_Number']};{row['Email_Id']};{row['Phone_Number']}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    
    img.save(f"qr_codes/qr_code_{row['Unique_Number']}.png")
    print(f"QR code created for {row['Name']}")

for _, row in spreadsheet.iterrows():
    create_qr(row)

print("QR codes have been generated and saved in the 'qr_codes' directory.")
