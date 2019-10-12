from Requests import Requests
from bs4 import BeautifulSoup as BeautifulSoup

class Provider:
    def __init__(self, url):
        self._url = url
        self._proxies = []
    def getUrl(self):
        return self._url
    def getProxies(self):
        return self._proxies
    def updateProxies(self):
        raise NotImplementedError
    def showProxies(self):
        raise NotImplementedError

class SSLProxies(Provider):
    url = "https://www.sslproxies.org"
    def __init__(self):
        super().__init__(SSLProxies.url)
    def updateProxies(self):
        updated = False
        self._proxies = []
        requestText = Requests.getText(self.getUrl())
        if requestText != None:
            soup = BeautifulSoup(requestText, "html.parser")
            table = soup.find("table", {"id": "proxylisttable"})
            if table != None:
                soup = BeautifulSoup(str(table), "html.parser")
                tableBody = soup.find("tbody")
                if tableBody != None:
                    soup = BeautifulSoup(str(tableBody), "html.parser")
                    tableRows = soup.find_all("tr")
                    if tableRows != None:
                        for i in tableRows:
                            soup = BeautifulSoup(str(i), "html.parser")
                            rowColumns = soup.find_all("td")
                            if rowColumns != None and len(rowColumns) >= 5:
                                self._proxies.append((str(rowColumns[0]) + ":" + str(rowColumns[1]) + "#" + str(rowColumns[2]) + "#" + str(rowColumns[4])).replace("<td>", "").replace("</td>", ""))
                        updated = True
        if not updated:
            self._proxies = []
    def showProxies(self):
        for i in self._proxies:
            print(i)

class SocksProxy(Provider):
    url = "https://www.socks-proxy.net"
    def __init__(self):
        super().__init__(SSLProxies.url)
    def updateProxies(self):
        updated = False
        self._proxies = []
        requestText = Requests.getText(self.getUrl())
        if requestText != None:
            soup = BeautifulSoup(requestText, "html.parser")
            table = soup.find("table", {"id": "proxylisttable"})
            if table != None:
                soup = BeautifulSoup(str(table), "html.parser")
                tableBody = soup.find("tbody")
                if tableBody != None:
                    soup = BeautifulSoup(str(tableBody), "html.parser")
                    tableRows = soup.find_all("tr")
                    if tableRows != None:
                        for i in tableRows:
                            soup = BeautifulSoup(str(i), "html.parser")
                            rowColumns = soup.find_all("td")
                            if rowColumns != None and len(rowColumns) >= 5:
                                self._proxies.append((str(rowColumns[0]) + ":" + str(rowColumns[1]) + "#" + str(rowColumns[2]) + "#" + str(rowColumns[4])).replace("<td>", "").replace("</td>", ""))
                        updated = True
        if not updated:
            self._proxies = []
    def showProxies(self):
        for i in self._proxies:
            print(i)
