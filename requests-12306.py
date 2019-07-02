import requests


def main():
    url = "https://https://www.icbc.com.cn/icbc/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    proxy = {
        "http": "http://113.121.21.19:9999"
    }
    resp = requests.get(url, headers=header, proxies=proxy, verify=False)
    print(resp)
    print(resp.status_code)
    data = resp.content.decode("utf-8")
    with open("11.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
