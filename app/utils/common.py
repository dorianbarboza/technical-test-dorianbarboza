
import boto3
import logging
from botocore.exceptions import ClientError
from typing import List, Optional
from app.core.config import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

from app.core.config import AWS_REGION



logger = logging.getLogger(__name__)


def send_email(
    sender: str,
    recipients: List[str],
    subject: str,
    body_text: str,
    body_html: Optional[str] = None
) -> str:
    """
    Send an email using Amazon SES.

    :param sender: Verified email address in SES to be used as the sender.
    :param recipients: List of recipient email addresses.
    :param subject: Subject of the email.
    :param body_text: Plain text version of the email body.
    :param body_html: HTML version of the email body (optional).
    :return: MessageId if the email was sent successfully.
    :raises RuntimeError: If the email could not be sent.
    """

    ses_client = boto3.client(
        "ses", region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    message = {
        "Subject": {"Data": subject, "Charset": "UTF-8"},
        "Body": {"Text": {"Data": body_text, "Charset": "UTF-8"}},
    }

    if body_html:
        message["Body"]["Html"] = {"Data": body_html, "Charset": "UTF-8"}

    try:
        response = ses_client.send_email(
            Source=sender,
            Destination={"ToAddresses": recipients},
            Message=message,
        )
        return response["MessageId"]

    except ClientError as e:
        logger.error("Error sending email: %s", e.response["Error"]["Message"])
        raise RuntimeError("Failed to send email with SES") from e
