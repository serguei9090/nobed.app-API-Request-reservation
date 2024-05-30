import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(booking_body):
    """
    Sends an email using Gmail's SMTP server with authentication.

    Args:
        sender_email (str): Email address of the sender (Gmail address).
        sender_password (str): Password for the sender's Gmail account.
        recipient_email (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body of the email (plain text or HTML).

    Returns:
        None

    Raises:
        Exception: If an error occurs during email sending.
    """
    try:
        # Example usage (replace with your actual credentials)
        sender_email = "serguei246@gmail.com"
        sender_password = "kxoz utrz mtxs sbng"  # Use App Password if 2FA is enabled
        recipient_email = "serguei246@gmail.com"
        subject = "Test Email (using smtplib)"
        body = booking_body
        
        # Create a MIME message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the HTML body to the email
        msg.attach(MIMEText(body, 'html'))
        
        # Create SMTP server connection (secured with SSL)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        
        # Login with authentication
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")