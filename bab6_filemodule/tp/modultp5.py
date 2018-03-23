def ratarata(data):
    jml=0
    total=0
    for i in data:
        a=i[2]
        total=total+a
        jml=jml+1
    rata=total/jml
    return rata
