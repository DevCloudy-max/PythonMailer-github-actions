import smtplib

# 🚨 Hardcoded credentials
email = "admin@example.com"
password = "hardcodedpassword"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)  # CodeQL should flag this
