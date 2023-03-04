from bs4 import BeautifulSoup
import pandas as pd
import requests
index=[]
index_no=0
url="https://www.w3schools.com"
response=requests.get(url) 
bs= BeautifulSoup(response.text,'html.parser') 
courses = bs.find_all('div',{'class':'w3-col l3 m6'}) #or bs.find_all('div',{'class':'w3-hide-large w3-hide-small'})
for course in courses:
  content=course.find('h3',{'class':'w3-margin-top'})
  parts=course.find_all('a',{'class':'w3-bar-item w3-button'} )
  Part=[]
  Link=[]
  for part in parts:
    Part.append(part.text)
    link=url+part.get('href')
    Link.append(link)
    
  print(content.text)
  for i in range(0,len(Part)):
     if Part[i]=='Learn AI':
      print("Data Analytics\n\n\n")
     elif Part[i]=='Learn XML':
      print("XML\n\n\n")
     else:
      pass

     print(Part[i],":\t",Link[i])
  print('\n\n\n')


  
  #t=[content,Part,Link]
  #index.append(t)
  #index_no+=1
#index_df=pd.DataFrame(index, columns=['Heading','Sub_Heading','Link'])
#index_df.to_csv('W3Schools.csv')

  
  

       

