import requests

def check_proxy(ip):
    """第二种："""
    try:
        # 设置重连次数
        requests.adapters.DEFAULT_RETRIES = 3
        # IP = random.choice(IPAgents)
        proxy = f"http://{ip}"
        # thisIP = "".join(IP.split(":")[0:1])
        # print(thisIP)
        res = requests.get(url="http://icanhazip.com/",timeout=0.5, proxies={"http": proxy})
        proxyIP = res.text
        if (proxyIP != None or proxyIP!=""):
            return True
        else:
            return False
    except:
        return False
