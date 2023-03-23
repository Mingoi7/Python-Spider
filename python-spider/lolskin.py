import requests
from bs4 import BeautifulSoup
import os

# get the specify lol champion with all skin by inputing the champion name
input_image = str(input("Enter Hero Name："))

response = requests.get("https://www.leagueoflegends.com/zh-tw/champions/"+input_image+"/")
soup = BeautifulSoup(response.text, "html.parser")

result = soup.select('div.eEYVgH img.dBitJH') 


count=0 
if not result :
    print(input_image,"is not a hero")

else :

    if not os.path.exists("img"):
        os.mkdir("img")
        

    if not os.path.exists("img/"+input_image):
        os.mkdir("img/"+input_image)
        
        for i in result:
            count+=1
            print("Picture",count,":",i["src"])
            pic=requests.get(i["src"])
            img = pic.content
            pic_out = open("img/"+input_image+"/"+str(count)+".png",'wb')
            pic_out.write(img)
            pic_out.close()

    else:
        print("You already have "+input_image+" skin picture")
