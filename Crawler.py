import requests
from bs4 import BeautifulSoup

url = 'https://www.digikala.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
for link in soup.find_all('a'):
    if isinstance(link,str):
        urls.append(link)
file1 = open("digikala.txt", "w")
count=1
product_links=[]
page_num=[]
flag=True
temp=1
key_id=1
page_num.append(temp)
while (len(page_num)!=0):
    for element in urls:
        if isinstance(element,str):
            if "/product/" in element:
                if count>=2:
                    cursor = conn.execute("SELECT id, product_link from products")
                    for row in cursor:
                        link1=row[1]
                        id1=row[2]
                        if link1==element:
                            conn.execute("INSERT INTO links (source,destination) VALUES (?,?)", (temp,id1))
                            file1.write(str(temp) + " " + str(id1) + '\n')
                        flag=False
                elif count==1 or flag==True:
                    key_id+=1
                    conn.execute("INSERT INTO products(id,product_link) VALUES (?,?)", (key_id,element))
                    page_num.append(key_id)
                    product_links.append(element)
                    conn.execute("INSERT INTO links (source,destination) VALUES (?,?)", (temp,key_id))
                    file1.write(str(temp) + " " + str(key_id) + '\n')
    r_link=page_links.pop()
    temp=page_num.pop()
    count+=1
    reqs = requests.get(r_link)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        if isinstance(link,str):
            urls.append(link)
file1.close()
conn.commit()
conn.close()
