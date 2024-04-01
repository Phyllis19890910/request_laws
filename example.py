import requests
items=[]
url='https://flk.npc.gov.cn/api/?type=flfg&xlwj=05&searchType=title%3Baccurate&sortTr=f_bbrq_s%3Bdesc&gbrqStart=&gbrqEnd=&sxrqStart=&sxrqEnd=&sort=true&page=1&size=10&_=1654157294070'
r=requests.get(url)
