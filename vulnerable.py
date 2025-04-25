import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ❌ Hardcoded credentials (vulnerability)
sender_email = "hardcoded.email@gmail.com"
sender_password = "weakpassword123"
receiver_email = "victim@example.com"

# ❌ Function with insecure handling of sensitive information
def sendmail(workflow_name, repo_name, workflow_run_id):
    # ❌ No input validation or sanitization
    subject = f"Workflow {workflow_name} has failed for repo {repo_name}"
    body = f"""
    Hi,

    The workflow {workflow_name} has failed for repo {repo_name}.
    Please check the logs for more details.

    Thanks,
    Run_ID: {workflow_run_id}
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # ❌ Unverified SMTP connection (no certificate check)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # no SSL/TLS cert verification
        server.login(sender_email, sender_password)  # weak, hardcoded password used
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print('email sent successfully')
    except Exception as e:
        # ❌ Generic exception handling
        print(f"Error: {e}")
        print('email not sent')

# ❌ Exposing function call without protective check (like __name__ == "__main__")
sendmail("dangerous_workflow", "insecure_repo", "98765")
