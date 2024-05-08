import urllib.request

with open("everything.txt", "r") as f:
    everything = [i.strip() for i in f.read().splitlines()]
    
    for idx, i in enumerate(everything):
        r = urllib.request.urlopen(i).read()
        with open(f"./assets/{idx}.jpg", "wb") as f:
            f.write(r)