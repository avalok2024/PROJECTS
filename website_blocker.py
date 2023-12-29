import datetime
import time

end_time = datetime.datetime(2023, 12, 30)
site_block = ["https://www.youtube.com/"]
hosts_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start blocking")
        with open(hosts_path, "r+") as hosts_file:
            content = hosts_file.read()
            for website in site_block:
                if website not in content :
                    hosts_file.write(redirect + " " +website+"\n")
                else:
                    pass
    else:
        with open(hosts_path, "r+") as hosts_file:
            content = hosts_file.readlines()
            hosts_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    hosts_file.write(lines)


            hosts_file.truncate()

        time.sleep()


