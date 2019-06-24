import urllib.request
from http import cookiejar
from urllib import parse


def main():
    # 5E38C50D5B
    '''
    username: sinaawp@163.com
pwd: ly16132651
formhash: F2A0665B41
backurl: https%3A%2F%2Fwww.yaozh.com%2Fmember%2F
    '''
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    login_url = "https://www.yaozh.com/login"
    login_form_data = {
        "username": "sinaawp@163.com",
        "pwd": "ly16132651",
        "formhash": "5E38C50D5B",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    cook = cookiejar.CookieJar()

    handler = urllib.request.HTTPCookieProcessor(cook)

    opener = urllib.request.build_opener(handler)

    login_str = parse.urlencode(login_form_data).encode("utf-8")
    login_request = urllib.request.Request(login_url, headers=header, data=login_str)

    resp = opener.open(login_request)
    print(resp)
    data = resp.read().decode("utf-8")
    # print(data)

    member_url = "https://www.yaozh.com/member/"
    member_request = urllib.request.Request(member_url, headers=header)
    data = opener.open(member_request).read().decode("utf-8")
    with open("08.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
