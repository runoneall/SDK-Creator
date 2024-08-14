import requests

def SendGet(url:str, headers:dict):
    response = requests.get(url, headers=headers)
    return response

def SendPost(url:str, headers:dict, data:any):
    response = requests.post(url, headers=headers, data=data)
    return response