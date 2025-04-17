import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Notifier:
    def __init__(self, email_host, email_port, sender_email, sender_password):
        self.email_host = email_host
        self.email_port = email_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_email_notification(self, recipient_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            with smtplib.SMTP_SSL(self.email_host, self.email_port) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
    
    def send_slack_notification(self, slack_webhook_url, message):
        import requests
        payload = {"text": message}
        response = requests.post(slack_webhook_url, json=payload)
        if response.status_code == 200:
            print("Slack notification sent successfully")
        else:
            print(f"Failed to send Slack notification: {response.status_code}")

# 示例用法
if __name__ == "__main__":
    notifier = Notifier(
        email_host="smtp.gmail.com", 
        email_port=465, 
        sender_email="your_email@gmail.com", 
        sender_password="your_email_password"
    )
    notifier.send_email_notification("recipient@example.com", "Test Subject", "This is a test email.")
