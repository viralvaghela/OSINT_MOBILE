import requests
def check_instagram(num):
    import requests

    burp0_url = "https://www.instagram.com:443/api/v1/web/accounts/account_recovery_send_ajax/"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Csrftoken": "bShw46OB35NJxqZhWDt3WWBwq3ZjfIlX", "X-Instagram-Ajax": "1008400429", "X-Ig-App-Id": "936619743392459", "X-Asbd-Id": "129477", "X-Ig-Www-Claim": "0", "X-Web-Device-Id": "4946C9B5-839D-4132-B16E-76DEF3ED9FF9", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.instagram.com", "Referer": "https://www.instagram.com/accounts/password/reset/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    burp0_data = {"email_or_username":num}
    res=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
    jsonData= res.json()
    if(jsonData['status']=="ok"):
        print("Instagram : True")
    else:
        print("Instagram : False")
