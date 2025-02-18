import smtplib
from email.mime.text import MIMEText        # MIMEText is a class
from email.mime.multipart import MIMEMultipart # MIMEMultipart is a class
import os
def sendmail(workflow_name,repo_name,workflow_run_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')


    #email massage
    subject = f"Workflow {workflow_name} has failed for repo {repo_name}"
    body = f"Hi, \n\nThe workflow {workflow_name} has failed for repo {repo_name}. Please check the logs for more details.\n\nThanks \nRun_ID: {workflow_run_id}"


    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    #send email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('email sent')
        server.quit()

        print('email sent successfully')
    except Exception as e:
        print(f"Error: {e}")
        print('email not sent')

sendmail(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))