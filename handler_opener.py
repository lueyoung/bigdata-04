import urllib.request


def main():
    url = "https://blog.csdn.net/u012195214/article/details/78889602"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    handler = urllib.request.HTTPHandler()

    opener = urllib.request.build_opener(handler)

    resp = opener.open(url)

    print(resp)

    data = resp.read().decode("utf-8")

    with open("05.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
