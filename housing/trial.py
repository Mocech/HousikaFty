import smtplib

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "mosesfrancis018@gmail.com"
EMAIL_HOST_PASSWORD = "xcuw agig iayy wnka"

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()

try:
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("✅ Login successful!")
except smtplib.SMTPAuthenticationError as e:
    print("❌ Login failed:", e)
finally:
    server.quit()
