import smtplib as s

smt = s.SMTP("smtp@gmail.com", 587)
smt.ehlo()
smt.starttls()
smt.login("obiumnights@gmail.com", "password of email")
subjects = "Test python program"
body = "We are working!"
massage = "subjects:{} \n\n {}".format(subjects, body)
list_add = ["av1662005@gmail.com", "minestream63@gmail.com"]
smt.sendmail("obiumnights@gmail.com", list_add, massage)
print("SENT MASSAGE")

smt.quit()


