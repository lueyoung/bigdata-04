import urllib.request
import urllib.parse
import string


def main():
    # base url
    url = "http://www.baidu.com/s?wd="
    print(url)

    # string append
    url += "大数据"
    # url += "%E5%A4%A7%E6%95%B0%E6%8D%AE"
    print(url)
    # 中文 -> ascii
    url = urllib.parse.quote(url, safe=string.printable)
    print(url)

    # open url, return response
    resp = urllib.request.urlopen(url)

    # read从resp中读数据（bytes），decode：byte -> string
    data = resp.read().decode("utf-8")  # byte -> string

    print(resp)
    # print(data)
    # save data
    with open("01.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
