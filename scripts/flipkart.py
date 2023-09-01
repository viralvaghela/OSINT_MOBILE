import requests

def check_flipkart(num):
    num = "+91"+num
    
    burp0_url = "https://1.rome.api.flipkart.com:443/api/6/user/signup/status"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Referer": "https://www.flipkart.com/", "X-User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0 FKUA/website/42/website/Desktop", "Origin": "https://www.flipkart.com", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "Te": "trailers", "Connection": "close"}
    burp0_json={"loginId": [num], "supportAllStates": True}
    
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    jsonData= response.json()
    jsonData['RESPONSE']['userDetails'][num]
    
    if(jsonData['RESPONSE']['userDetails'][num]=="GUEST"):
        print("Flipkart : False")

    elif(jsonData['RESPONSE']['userDetails'][num]=="VERIFIED"):
        print("Flipkart : True")

    elif(jsonData['RESPONSE']['userDetails'][num]=="VERIFIED"):
        print("Flipkart : True")
    else:
        print("Flipkart : False")