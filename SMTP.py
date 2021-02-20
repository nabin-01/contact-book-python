import smtplib as smtp
import ssl as ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# This class handles all SMTP interactions via the smtplib & ssl libraries
class SMTP:
    # This function is called when the SMTP class is instantiated
    # Fetches user credentials to log into SMTP server, establishes secure connection via TLS & tests the integrity of the connection
    def __init__(self):
        self.smtp = "smtp.gmail.com" # using gmail smtp server for development purposes
        self.port = 587
        self.user_email = 1 # TODO: User email input when application starts (for SMTP login)
        self.password = 1 # TODO: User password input when application starts (for SMTP login)
        self.recipient_email = 1 # TODO: Fetch Recipient email(s) from GUI as defined by user 
        self.ssl_context = ssl.create_default_context()

        # Test integrity of connection, if connection is not established properly print error messages for traceback
        try:
            server = smtp.SMTP(self.smtp, self.port)
            server.starttls(context = self.ssl_context)
            server.login(self.user_email, self.password)
        except Exception as e:
            print(e)
        finally:
            server.quit()
    
    # This functions connects to the SMTP server defined in __init__ & sends the user's message to the selected contact(s)
    def send(self):
        server = smtp.SMTP(self.smtp, self.port)
        server.starttls(context = self.ssl_context)
        server.login(self.user_email, self.password)

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.user_email
        self.message["To"] = self.recipient_email
        self.text = """ TEST """ # TODO: Fetch plain text version of the message from GUI
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

        server.sendmail(self.user_email, self.recipient_email, self.message.as_string())
