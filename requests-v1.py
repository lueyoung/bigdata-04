import requests


def main():
    url = "https://www.baidu.com"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    resp = requests.get(url, headers=header)
    print(resp)
    print(resp.status_code)
    data = resp.content.decode("utf-8")
    print(data)


if __name__ == "__main__":
    main()
