

from app.utils.common import send_email
from app.core.config import EMAIL_ADMIN, EMAIL_SENDER

def notify_admins(to_emails: tuple, message: str):
    """
    Builds and sends a notification email to the Admins using SES.
    """
    
    subject = "🚨 Admin Notification"
    body_text = "Hello Admins,\n\nThis is an automated notification from the system."
    body_html = f"""<html>
    <head></head>
    <body>
      <h2>Hello Admins,</h2>
      <p>{message}</p>
    </body>
    </html>"""

    message_id = send_email(
        sender=EMAIL_SENDER,
        recipients=to_emails,
        subject=subject,
        body_text=body_text,
        body_html=body_html,
    )

    print(f"✅ Admins notified. Message ID: {message_id}")




if __name__ == "__main__":
    notify_admins()
