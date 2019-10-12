import ProxyProviders
import sys

def main():
    if len(sys.argv) == 2:
        if(sys.argv[1] == "--https"):
            httpsProxy = ProxyProviders.SSLProxies()
            httpsProxy.updateProxies()
            httpsProxy.showProxies()
        elif(sys.argv[1] == "--socks4"):
            socks4Proxy = ProxyProviders.SocksProxy()
            socks4Proxy.updateProxies()
            socks4Proxy.showProxies()
        else:
            print("Avaible Commands: \n--https: List HTTPs based proxies\n--socks4: List Socks4 based proxies")
    else:
        print("Execute --help to learn how to use me")
if __name__ == "__main__":
    main()
