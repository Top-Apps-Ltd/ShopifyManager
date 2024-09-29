import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email( WatchModel, Quantity):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to your Gmail account with the app password
        server.login(from_email, app_password)
        
        # Send the email
        server.send_message(msg)
        
        # Disconnect from the server
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    from_email = 'shayfarh3475@gmail.com'
    to_email = 'mamanon3235@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email ya homo.'
    app_password = 'awbb szjb xlsb rmeq'  # Use the app-specific password

