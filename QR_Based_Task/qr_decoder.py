import cv2
from pyzbar.pyzbar import decode
import pandas as pd
import numpy as np
import datetime

# Path to the Excel sheet to track entries (Replace "path_to_excel.xlsx" with the actual path)
excel_file = "path_to_excel.xlsx"

cap = cv2.VideoCapture(0)

try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Unique Number", "Email", "Phone", "Timestamp"])
    df.to_excel(excel_file, index=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    decoded_objects = decode(frame)
    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8")
        
        qr_parts = qr_data.split(';')
        if len(qr_parts) == 4:
            name, unique_number, email, phone = qr_parts
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if name in df['Name'].values:
                cv2.putText(frame, f"{name} has already entered", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            else:
                new_entry = {"Name": name, "Unique Number": unique_number, "Email": email, "Phone": phone, "Timestamp": timestamp}
                df = df.append(new_entry, ignore_index=True)

                df.to_excel(excel_file, index=False)

                cv2.putText(frame, f"{name} has been marked as entered at {timestamp}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        else:
            cv2.putText(frame, "Invalid QR Code data format.", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        points = obj.polygon
        if points:
            pts = [(point.x, point.y) for point in points]
            pts = np.array(pts, dtype=np.int32)
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
