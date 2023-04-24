from twilio.rest import Client
import config


def send_sms(sms_text: str, to_number: str) -> None:
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=f"{sms_text}",
                         from_=f"{config.my_twilio_phone_number}",
                         to=f"{to_number}"
                     )

    print(message.sid)
    print("Sms sanded successfully", sms_text, to_number)
