# ------------------------------ Resources ------------------------------ #
import smtplib as sl

# ------------------------------ Class ------------------------------ #


class NotificationManager:
    my_email = "sktest1025@gmail.com"
    my_password = "heyyouguys"
    # This class is responsible for sending notifications with the deal flight details.

# ------------------------------ Functions ------------------------------ #
    def send_message(self, message):
        """Sends cheap flight alerts via e-mail."""
        with sl.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs="ScottKostolni@gmail.com",
                                msg=f"Subject:Cheap Flight Alert!\n\n {message}")