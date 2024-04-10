from pyscript import document
import json
from pyodide.http import pyfetch
import asyncio

USERS = "./users/users.json"

async def getSessionKey(accessCode:str, secretCode:str)->str:
    url = f"https://www.wikiart.org/en/Api/2/login?accessCode={accessCode}&secretCode={secretCode}"
    
    response = await pyfetch(url=url)
    data = response.json()
    if "SessionKey" in data.keys():
        return data["SessionKey"]
    else:
        print(f"WARNING: Session Key not in response -- {data}")
    
    return None

def getImageItem(imgURL:str) -> str:
    html = '<div class="image-div">'
    html += f'<img src="{imgURL}">'
    html += '<button><img src="./images/tup.png"></button><button><img src="./images/tdn.png"></button></div>'
    return html

def startClassifying(event):
    print("classifying")

async def login(event):
    userN = document.querySelector("#username").value
    passW = document.querySelector("#password").value
    loginStatusDiv = document.querySelector("#login-status")
    #loginStatusDiv.innerText = f"u: {userN}, p: {passW}"
    url = f"http://cs.uky.edu/~arbarr3/login.php?username={userN}&password={passW}"
        
    resp = await pyfetch(url=url)
    resp = await resp.json()
    accessCode = resp["accessCode"]
    secretCode = resp["secretCode"]
    #sessionKey = await getSessionKey(accessCode, secretCode)
    #print(sessionKey)
    document.querySelector("#step1").classList.add("hidden")
    document.querySelector("#step2").classList.remove("hidden")
    imageRow = document.querySelector("#images")
    allImages = ""
    for i in range(5):
        allImages += getImageItem("images/ares_logo.png")
    imageRow.innerHTML = allImages
    
