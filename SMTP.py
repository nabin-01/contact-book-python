import smtplib as smtp
import ssl as ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SMTP:
    # Defining constuctor for SMTP class
    def __init__(self):
        # Defining a bunch of class variables
        self.smtp = "smtp.gmail.com"  # using gmail smtp server for development purposes
        self.port = 587
        self.user_email = 1  # TODO: User email input when application starts (for SMTP login)
        self.password = 1  # TODO: User password input when application starts (for SMTP login)
        self.recipient_email = 1  # TODO: Fetch Recipient email(s) from GUI as defined by user
        self.ssl_context = ssl.create_default_context()
        self.server = smtp.SMTP(self.smtp, self.port)

        # Test the connection to smtp server
        try:
            self.server.starttls(context=self.ssl_context)
            self.server.login(self.user_email, self.password)
        # Return errors for traceback
        except Exception as e:
            return e
        # If connection is established succesfully, close the connection
        finally:
            self.server.quit()

    # Re-connect to SMTP server with already tested connection & send email
    def send(self):
        self.server = smtp.SMTP(self.smtp, self.port)
        self.server.starttls(context=self.ssl_context)
        self.server.login(self.user_email, self.password)

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.user_email
        self.message["To"] = self.recipient_email
        self.text = """ TEST """  # TODO: Fetch plain text version of the message from GUI
        self.html = """ <html>
                                <body>
                                    <h1> HTML TEST <h1>
                                </body>
                            </html> 
                            """
        # TODO: Fetch html version of the message from GUI
        self.plaintext = MIMEText(self.text, "plain")
        self.htmltext = MIMEText(self.html, "html")
        self.message.attach(self.plaintext)
        self.message.attach(self.htmltext)

        self.server.sendmail(self.user_email, self.recipient_email, self.message.as_string())