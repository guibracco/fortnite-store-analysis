import os
from bs4 import BeautifulSoup
import pandas

df = pandas.DataFrame()

print("Parsing...")

folder_path = os.path.dirname(__file__)
input_path = folder_path + "/pages"

html_file_paths = os.listdir(input_path)

with open(folder_path + "/csv/" + "store.csv", "w") as outfile: 
    outfile.write(f"date,rarity,item_type,name,cost\n")
    
    html_file_paths = os.listdir(input_path)
    
    for path in html_file_paths:
        with open(input_path + "/" + path, "r") as infile: 
            soup = BeautifulSoup(infile, features="html.parser")
            html_items = soup.main.find_all("div", "item-responsive")

            for html_item in html_items:
                # print(html_item.prettify()) # If you want to look a html
                
                try:
                    date = path.split(".")[0]
                    rarity = html_item.a["class"][2].strip().split("-")[1]
                    item_type = html_item.a["href"].split("/")[1].strip()
                    name = html_item.span.text.strip()

                    # Try to parse the cost, set to -1 if parsing fails
                    try:
                        cost = int(html_item.p.text.strip().replace(",",""))
                    except ValueError:
                        cost = -1

                    # print(date, rarity, item_type, name, cost)
                    outfile.write(f"{date},{rarity},{item_type},\"{name}\",{cost}\n")
                except Exception as e:
                    print("Error processing item:", e, html_item.prettify())
