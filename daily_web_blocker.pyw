import time
from datetime import datetime as dt



'''Create a website blocker which is blocking the acces to desired website during a desired schedule
by editing the hosts file (found in hosts_path variable)'''


hosts_path =r"C:\Windows\System32\drivers\etc\hosts"  # in order to acces the blocking website txt file
redirect = "127.0.0.1"  # in case you acces a blocked website you will be re-direct on local host page
website_list = ["www.facebook.com", "facebook.com", "www.mmohut.com", "mmohut.com"]  # blocked website list

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,
          8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):  # check if we are in the working hours
        print("12231")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write('   ' + redirect + '    ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
