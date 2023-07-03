
import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials


def create_image_attachment(path: str) -> MIMEImage:
    with open(path, "rb") as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header("Content-Disposition", f"attachment; filename={path}")
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = "smtp-mail.outlook.com"
    port: int = 587
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP(host, port) as server:
        print("Logging in...")
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(credentials.EMAIL, credentials.PASSWORD)
        
        # Prepare the email
        print("Attempting to send the email...")
        message = MIMEMultipart()
        message["From"] = credentials.EMAIL
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)
        
        server.sendmail(from_addr=credentials.EMAIL, to_addr=to_email, msg=message.as_string())
        
        print("Sent!")


if __name__ == "__main__":
    send_email(to_email="test_email@yettocreate.com", 
               subject="TEST",
               body="TESTING!",
               image="some.png")

