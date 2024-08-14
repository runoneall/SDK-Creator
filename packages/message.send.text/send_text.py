import json
SDK_Class = type('SDK_Class', (), {})

def send(token:str, recvId: str, recvType: str, text: str, buttons: list = []):
    data = {
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "text",
        "content": {
            "text": text,
            "buttons": [buttons]
        }
    }
    rep = SDK_Class.netool.SendPost(
        url=f'https://chat-go.jwzhd.com/open-apis/v1/bot/send?token={token}', 
        headers={"Content-Type": "application/json; charset=utf-8", }, 
        data=json.dumps(data)
    )
    return json.loads(rep.text)