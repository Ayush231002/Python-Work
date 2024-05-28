import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def calculate_date_difference(user_date):
    current_date = datetime.now().date()
    user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
    
    difference = (user_date - current_date).days
    return difference

def send_gmail_alert():
    # Gmail SMTP server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # TLS Port

    # Gmail account credentials
    sender_email = 'Email'
    sender_password = 'password'

    # Recipient email address
    recipient_email = 'Send mail'

    # Create a message
    message = MIMEText('Your certificate Expire is less than 30 days!')

    # Add sender, recipient, and subject to the email
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'Certificate Alert:Expire Less than 30 Days Remaining'

    # Connect to Gmail SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def main():
    user_input = input("Enter a date (YYYY-MM-DD): ")
    try:
        days_difference = calculate_date_difference(user_input)
        print("The difference in days between the input date and the current date is:", days_difference)
        if days_difference < 30:
            send_gmail_alert()
            print("Gmail alert sent!")
        else:
            print("No need to send an alert.")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()
