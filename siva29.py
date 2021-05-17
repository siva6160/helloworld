from array import*

vals=array('i',[2,5,7,9,11,61,17,55,61])
newarr=array(vals.typecode,(a*a for a in vals))
for i in newarr:
    print(i)
