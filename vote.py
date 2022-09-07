import requests

payload = {'entryid': 681, 'freeVoteCode': ''}
url = 'https://smartfilms.com.co/votaciones/film/681'
post_url = 'https://smartfilms.com.co/votaciones/submit-vote'

r = requests.get(url)
cookies_dict = r.cookies.get_dict()
third_cookie = ""

for cookie_key in cookies_dict.keys():
    if len(cookie_key) > 20:
        third_cookie += cookie_key

cookie = f"XSRF-TOKEN={cookies_dict.get('XSRF-TOKEN')}; smartfilms_session={cookies_dict.get('smartfilms_session')}; {third_cookie}={cookies_dict.get(third_cookie)}"

headers = {
    "authority": "smartfilms.com.co",
    "method": "POST",
    "path": "/votaciones/submit-vote",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en,es;q=0.9",
    "content-length": "35",
    "content-type": "application/json",
    "cookie": f"{cookie}",
    "dnt": "1",
    "origin": "https://smartfilms.com.co",
    "referer": "https://smartfilms.com.co/votaciones/film/681",
    "sec-ch-ua": 'Chromium v = "104", " Not A;Brand" v = "99", "Google Chrome" v = "104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "x-csrf-token": "C7itU4xywTwh3utY4Hr3yCkfI3QL6nZlA078Kh85"
}

r = requests.post(post_url, headers=headers, data=payload)
print(r.text)
