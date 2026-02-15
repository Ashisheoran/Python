import requests
import threading

urls =[
     "https://tse3.mm.bing.net/th/id/OIP.valnM8bFdPFYIKnRjZKrKwHaLG?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
     "https://tse2.mm.bing.net/th/id/OIP.1gqxePGrU4JMYrWZJy1XaQAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
]

def download_image(url,index):
    try:
        data = requests.get(url)
        if data.status_code == 200:
            with open(f"image{index}.jpg",'wb') as file:
                file.write(data.content)
            print(f"image{index}.jpg downloaded")
        else:
            print(f"Image{index} download fail")
    except Exception as e:
        print(f"Error in download {url} : {e}")
    
thread = []
for i,url in enumerate(urls):
    t = threading.Thread(target=download_image,args=(url,i))
    t.start()
    thread.append(t)
for t in thread:
    t.join()