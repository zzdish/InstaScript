import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Function to check Instagram account status
def is_instagram_account_active(username):
    url = f'https://www.instagram.com/{username}/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # The account is active
            return True
        else:
            # The account is not active
            return False
    except Exception as e:
        print(f"Error checking Instagram account: {e}")
        return False

# Function to send email notification
def send_email_notification(to_email, subject, message):
    from_email = "michaeljones.mj786@gmail.com"
    from_password = "ashish@0951"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Monitoring loop
def monitor_instagram_account(username, check_interval, recipient_email):
    was_inactive = not is_instagram_account_active(username)
    while True:
        is_active = is_instagram_account_active(username)
        if is_active and was_inactive:
            # The account just became active
            send_email_notification(
                recipient_email,
                f"{username} is now active on Instagram!",
                f"The Instagram account {username} is now active. Check it out: https://www.instagram.com/{username}/"
            )
            was_inactive = False  # Update the status
        elif not is_active:
            was_inactive = True  # Account is still inactive

        # Wait for the specified interval before checking again
        time.sleep(check_interval)

# Replace with the Instagram username you want to monitor
instagram_username = "deeeeeeeeeeeeeeksha"

# Replace with the email address to send the notification to
recipient_email = "ashish.parker1999@gmail.com"

# Set the check interval in seconds (e.g., 3600 seconds = 1 hour)
check_interval = 3600

# Start monitoring the Instagram account
monitor_instagram_account(instagram_username, check_interval, recipient_email)
