import datasets
import collections
import glob
import pandas as pd
import re
c = collections.Counter()

#for name in glob.glob("pyprolog-asts/*")[0:3]: # test with only 3 files
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
#if "type" in k:
                if True:
                    #_type = s[k])
                    v = i[k][0] # get the value
                    k2 = re.sub("\d+", "N", k)
                    if isinstance(v, (str,float,int)):
                        # skip none and []
                        c[k2]+=1
        
df = pd.DataFrame.from_dict(c, orient='index').reset_index().sort_values(by=0, ascending=False)
df.to_csv("report_without_numbers_sorted.csv")
#for x in c.most_common():
#    print(x)
