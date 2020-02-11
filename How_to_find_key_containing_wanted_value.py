thisdict = {'george':16,
            'amber':19}
search_age = 16

# Method 1
for name, age in thisdict.items():
    print(list(thisdict.keys())[list(thisdict.values()).index(search_age)])


# Method 2
for name, age in thisdict.items():
    if age == search_age:
        print name