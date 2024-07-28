import datasets
import collections
import glob

c = collections.Counter()
for name in glob.glob("pyprolog-asts/*"):
    try:
        ds = datasets.load_from_disk(name)
    except FileNotFoundError as e:
        continue # not a dataset
    for x in ds:
        print (x)
        ds2 =ds[x]
        iter=ds2.iter(batch_size=1)
        for i in iter:
            for k in i:
                if "type" in k:
                    _type = str(i[k][0])
                    c[k]+=1

for x in c.most_common():
    print(x)
