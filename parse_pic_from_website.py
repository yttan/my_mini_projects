"""Pasre pictures from a Baidu Tieba website and save them in testfolder"""
import requests
from bs4 import BeautifulSoup
import shutil
resp = requests.get('http://tieba.baidu.com/p/2166231880')
soup = BeautifulSoup(resp.text)
imgtags = soup.find_all(name='img',attrs={"class": "BDE_Image"})
counter = 0
for tag in imgtags:
    print(tag.attrs['src'])
    url = tag.attrs['src']
    pic = requests.get(url,stream=True)
    counter = counter + 1
    save_path = "testfolder/"
    with open(save_path+str(counter)+".jpg",'wb') as f:
        pic.raw.decode_content = True
        shutil.copyfileobj(pic.raw, f)
    f.close()
