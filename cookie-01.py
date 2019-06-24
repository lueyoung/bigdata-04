import urllib.request


def main():
    url = "https://www.yaozh.com/member/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Cookie": "acw_tc=2f624a4915610792329614884e79c148700616d6ee5796260d1ba8edd1e3c6; _ga=GA1.1.508488396.1561079453; PHPSESSID=ff69uonsd20kn3qgscv2jfvuh5; _gid=GA1.2.242338926.1561357124; _gat=1; MEIQIA_VISIT_ID=1N53RovRvkLqeJW4pMgEc83C0Fs; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1561357126; yaozh_userId=773375; UtzD_f52b_saltkey=BCJ55eq5; UtzD_f52b_lastvisit=1561353529; yaozh_uidhas=1; yaozh_mylogin=1561357130; acw_tc=2f624a4915610792329614884e79c148700616d6ee5796260d1ba8edd1e3c6; _ga=GA1.1.508488396.1561079453; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1561079231%2C1561210358%2C1561357124; MEIQIA_VISIT_ID=1N53RovRvkLqeJW4pMgEc83C0Fs; UtzD_f52b_ulastactivity=1561024533%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D687557; UtzD_f52b_creditbase=0D0D6D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _gid=GA1.1.2063893204.1561357207; yaozh_logintime=1561357871; yaozh_user=773375%09sinaawp; db_w_auth=687557%09sinaawp; UtzD_f52b_lastact=1561357873%09uc.php%09; UtzD_f52b_auth=4544odm5g65rPcjc0xXdO%2BBJEyRoaziySqBO6XYb9sQSntlbLnn5eLXN1NwFHqf1dqLORdjDehrENf3J%2FsCm22zPQWM"
    }
    request = urllib.request.Request(url, headers=header)

    data = urllib.request.urlopen(request).read().decode("utf-8")
    with open("07.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
