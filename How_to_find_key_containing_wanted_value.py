thisdict = {'george':16,
            'amber':19}

#thisdict["brand"].append(["Sub", "Red"])
#print(thisdict["brand"])

search_age = 16
for name, age in thisdict.items():
    print(list(thisdict.keys())[list(thisdict.values()).index(search_age)])