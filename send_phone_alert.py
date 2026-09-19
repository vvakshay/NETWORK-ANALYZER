import requests
topic="TOPIC"
def send_phone_alert(message):
    URL=f"https://ntfy.sh/{topic}"
    try:
        response=requests.post(
            URL,
            data=message.encode("utf-8")
        )
        if response.status_code==200:
            print("PHONE ALERT SENT")
        else:
            print("PHONE ALERT FAILED",response.status_code)
    except Exception as e:
        print("Phone notification error:",e)

