import requests


def main():
    cookies = "acw_tc=2f624a4915610792329614884e79c148700616d6ee5796260d1ba8edd1e3c6; _ga=GA1.1.508488396.1561079453; PHPSESSID=5e31i7046c7v87cb1k9iqntkl6; _gid=GA1.2.1779263455.1561690613; _gat=1; MEIQIA_VISIT_ID=1NFxOSw04akrI42Q1NV03nrAUbE; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1561690618; yaozh_logintime=1561690619; yaozh_user=773375%09sinaawp; yaozh_userId=773375; db_w_auth=687557%09sinaawp; UtzD_f52b_saltkey=zY14rgd4; UtzD_f52b_lastvisit=1561687020; UtzD_f52b_lastact=1561690620%09uc.php%09; UtzD_f52b_auth=1262aGZJP7O3pLNN05wc6t5AzVojQtwpAHwArjuOdQKmuI6A6EkmF%2BIL%2BWY%2Fc6YiElpmf625IsJ3GZUOxKyqZy4ZEBw; yaozh_uidhas=1; yaozh_mylogin=1561690622; acw_tc=2f624a4915610792329614884e79c148700616d6ee5796260d1ba8edd1e3c6; _ga=GA1.1.508488396.1561079453; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1561359817%2C1561360080%2C1561360166%2C1561690613; MEIQIA_VISIT_ID=1NFxOSw04akrI42Q1NV03nrAUbE"
    print(type(cookies))
    cook_lst = cookies.split(";")
    cook_dict = {}
    print(type(cook_lst))
    print(cook_lst)
    for i in cook_lst:
        kv = i.strip()
        kv_lst = kv.split("=")
        k = kv_lst[0]
        v = kv_lst[1]
        cook_dict[k] = v
    print(cook_dict)
    url = "https://www.yaozh.com/member/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    resp = requests.get(url, headers=header, cookies=cook_dict)
    print(resp)
    print(resp.status_code)
    data = resp.content.decode("utf-8")
    with open("12.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
