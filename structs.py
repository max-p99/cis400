#read in csv
#lookup tags
#if match , ret img number fd

#ret set(fds)
import csv
def lookup(tags=[]):
    print(tags)
    imgs = set()
    with open('data.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for tag in tags:
                # print(row.keys())
                print(type(row["tags"]))

                if tag in row["tags"]:
                    imgs.add(row["file"])
    print(imgs)

    return list(imgs)

def tattoo_shop_find(strs):
    print(strs)
    shops = set()
    with open('tattoo_shops.csv', newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for strr in strs:
                if strr in row["spec"]:
                    print(row["spec"], "added", row["shop"] )
                    shops.add(row["shop"])
    print(shops)
    return list(shops)

def clean_tags(tags):
    return tags

def write_shop_to_csv(name, tags):
    cleaned = clean_tags(tags)

    csv_tags = ' '.join(cleaned)

    name = name.lower()
    with open('tattoo_shops.csv', 'a') as csvfile:
        csvfile.write(f"{csv_tags},{name}\n")

    return cleaned

write_shop_to_csv("eddite2",["animals", "people"])
# lookup(["cat","dog","kitten","animal"])
# tatoo_shop_find("fire")
#given img -> make tatoo rec
#hypernims
