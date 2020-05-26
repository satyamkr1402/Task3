import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("satyamsingh1402@gmail.com", "**********")


# message
message1 = "Accuracy is less than 90%.Please try again"

# sending the mail 
s.sendmail("satyamsingh1402@gmail.com", "satyamkr.gaya@gmail.com", message1)
    
# terminating the session 
s.quit()