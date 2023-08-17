import requests
from arrow.arrow import Arrow
import os
import datetime

# datetime.datetime(2020, 4, 17)
# First available date is 2017-10-30
date = Arrow.fromdatetime(datetime.datetime(2023, 8, 17))
folder_path = os.path.dirname(__file__)

# Going back from the date above, grab the pages in the range of days
for _ in range(365):
    url = "https://fnbr.co/shop/" + date.format("MMMM-DD-YYYY").lower()
    res = requests.get(url)
    if res.status_code == 200:
        f = open(folder_path + "/pages/" + date.format("YYYY-MM-DD") + ".html", "w")
        f.write(res.text)
        f.close()

    date = date.shift(days=-1)
