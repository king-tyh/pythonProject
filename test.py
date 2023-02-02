import chardet

a = "\u3010\u7f51\u7ad9\u54c1\u8d28\u3011"
print(a)
filename = "w3school.html"
open(filename, 'w', encoding="utf-8").write(a)

def check_proxy(ip, port):
    """第二种："""
    try:
        # 设置重连次数
        requests.adapters.DEFAULT_RETRIES = 3
        # IP = random.choice(IPAgents)
        proxy = f"http://{ip}:{port}"
        # thisIP = "".join(IP.split(":")[0:1])
        # print(thisIP)
        res = requests.get(url="http://icanhazip.com/", timeout=2, proxies={"http": proxy})
        proxyIP = res.text
        if (proxyIP == proxy):
            print("代理IP:'" + proxyIP + "'有效！")
            return True
        else:
            print("2代理IP无效！")
            return False
    except:
        print("1代理IP无效！")
        return False


