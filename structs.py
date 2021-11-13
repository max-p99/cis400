#read in csv
#lookup tags
#if match , ret img number fd

#ret set(fds)
import csv
def lookup(tags=[]):
    imgs = []
    with open('data.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for tag in tags:
                # print(row.keys())
                if tag in row["tags"]:
                    imgs.append(row["file"])
    print(imgs)
    return imgs
def tatoo_shop_find(str):
    shops = []
    with open('tattoo_shops.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if str in row["spec"]:
                shops.append(row["shop"])
    print(shops)
    return shops
lookup(["cat"])
tatoo_shop_find("fire")
#given img -> make tatoo rec
#hypernims
