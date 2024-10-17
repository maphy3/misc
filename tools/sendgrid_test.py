import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# SendGrid API キー
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# 送信するメールの情報
message = Mail(
    from_email='from@example.com',  # 送信元のメールアドレス
    to_emails='to@example.com',     # 送信先のメールアドレス
    subject='Email title',          # メールの件名
    html_content='<strong>and easy to do anywhere, even with Python</strong>'  # メール本文 (HTML)
)

try:
    # SendGrid API クライアントのインスタンスを作成し、メールを送信
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    
    # レスポンスを表示
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print(e)
