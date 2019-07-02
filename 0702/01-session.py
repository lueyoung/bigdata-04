import requests


def main():
    session = requests.session()
    login_url = "https://www.yaozh.com/login/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    # 36EE2E75A7
    login_form = {
        "username": "sinaawp@163.com",
        "pwd": "ly16132651",
        "formhash": "36EE2E75A7",
        "backurl": "https%2F%2Fwww.yaozh.com",
    }
    login_resp = session.post(login_url, headers=header, data=login_form)

    member_url = "https://www.yaozh.com/member/"
    data = session.get(member_url, headers=header).content.decode("utf-8")
    with open("01.html", "w", encoding="utf-8") as f:
        f.write(data)

if __name__ == '__main__':
    main()
