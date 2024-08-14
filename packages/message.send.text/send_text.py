import json

i=1
netool_post = None
Token = str()

def send(recvId: str, recvType: str, text: str, buttons: list = []):
    netool_post
    data = {
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "text",
        "content": {
            "text": text,
            "buttons": [buttons]
        }
    }
    rep = netool_post(
        url=f'https://chat-go.jwzhd.com/open-apis/v1/bot/send?token={Token}', 
        headers={"Content-Type": "application/json; charset=utf-8", }, 
        data=data
    )
    return json.loads(rep.text)