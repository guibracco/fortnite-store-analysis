import requests
from arrow.arrow import Arrow
import os
import datetime

# This script will crawl the fnbr.co item shop page and save the html for each day
# First available date is 2017-10-30
date = Arrow.fromdatetime(datetime.datetime(2023, 9, 18))
folder_path = os.path.dirname(__file__)

# Going back from the date above, grab the pages in the range of days
for _ in range(365):
    url = "https://fnbr.co/shop/" + date.format("MMMM-DD-YYYY").lower()
    res = requests.get(url)
    if res.status_code == 200:
        f = open(folder_path + "/html/" + date.format("YYYY-MM-DD") + ".html", "w")
        f.write(res.text)
        f.close()

    date = date.shift(days=-1)
