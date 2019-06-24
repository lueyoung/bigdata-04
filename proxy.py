import urllib.request

def main():
    # url
    url = "https://blog.csdn.net/u012195214/article/details/78889602"

    # user agent
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }

    # request
    request = urllib.request.Request(url,headers=header)

    # proxy
    proxy = {
        "http":"http://163.204.242.234:9999"
    }

    # build a proxy handler
    handler = urllib.request.ProxyHandler(proxy)

    # build a opener
    opener = urllib.request.build_opener(handler)

    # conn
    data = opener.open(request).read().decode("utf-8")

    with open("06.html","w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
