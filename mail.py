import tkinter as tk
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailApp:
    def _init_(self, master):
        self.master = master
        master.title("Mail Application")

        # create labels
        self.lbl_to = tk.Label(master, text="To:")
        self.lbl_to.grid(row=0, column=0, sticky="W")
        self.lbl_subject = tk.Label(master, text="Subject:")
        self.lbl_subject.grid(row=1, column=0, sticky="W")
        self.lbl_body = tk.Label(master, text="Body:")
        self.lbl_body.grid(row=2, column=0, sticky="W")

        # create entry fields
        self.entry_to = tk.Entry(master, width=50)
        self.entry_to.grid(row=0, column=1, columnspan=2)
        self.entry_subject = tk.Entry(master, width=50)
        self.entry_subject.grid(row=1, column=1, columnspan=2)
        self.entry_body = tk.Text(master, width=50, height=10)
        self.entry_body.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # create send button
        self.send_button = tk.Button(master, text="Send", command=self.send_mail)
        self.send_button.grid(row=4, column=1, sticky="E")

    def send_mail(self):
        # get data from entry fields
        sender_email = "your_email@example.com" # enter your email address here
        receiver_email = self.entry_to.get()
        password = "your_password" # enter your email password here
        subject = self.entry_subject.get()
        body = self.entry_body.get("1.0", tk.END)

        # create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # create SSL context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        # clear entry fields
        self.entry_to.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)
        self.entry_body.delete("1.0", tk.END)

root = tk.Tk()
app = MailApp(root)
root.mainloop()
