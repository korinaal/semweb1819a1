import csv

with open ("uri.csv", newline="", encoding="utf-8") as inputfile, open ("rdf.nt", "w", encoding="utf-8") as outputfile:
    reader = csv.reader(inputfile)

    for row in reader:
        s, p, o = row
        s = s.replace('b:', "_:")
        p = '<' + p + '>'
        if 'l:' in o:
            if 'Έναρξη' in p or 'Λήξη' in p:
                o = o+':00'
            o = o.replace('l:', '')
            o = '"'+o+'"'
        else: 
            o = '<' + o + '>'

        outputfile.write('{} {} {} .\n'.format(s, p, o))
