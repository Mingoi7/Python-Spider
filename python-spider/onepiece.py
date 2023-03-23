import requests
from bs4 import BeautifulSoup
import pandas as pd

#ONE PIECE
#List all people with their devilfruit 

d = {'名稱': [], '果實': []}
df = pd.DataFrame(data=d)
count = 0
pd.set_option('display.max_rows', 110)
pd.set_option('max_colwidth', 100)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


for page in range(1, 6):  
    response = requests.get("https://one-piece.com/log/character/devilfruit.html?p="+str(page))
    soup = BeautifulSoup(response.text, "html.parser")

    result = soup.select('span.detailBox') 

    for char in result :
        count+=1

        name = char.find('p',{'class':'charaName'}).getText()

        fruit = char.find('p',{'class':'f13 t subComment'}).getText()

        df.loc[count] = [name,fruit] 

df.to_csv('onepiece.csv')