for x in `cat files.txt`; do  dirname   $x; done | sort -u > paths.txt
for x in `cat ../paths.txt `; do echo $x; mkdir -p $x; done
find ./ -depth -name "*.prq" -exec sh -c 'mv "$1" "pyprolog-asts/${1%.prq}.parquet"' _ {} \;
mv pyprolog-asts/.venv pyprolog-asts/venv
