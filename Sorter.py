def sort_function(name):
    searchfile = open(name + ".json", "r")
    writefile = open(name + "_Sorted.json", "w")
    for line in searchfile:
            column = line.split() # split line into parts
            if len(column) > 6:   # checks for enough columns
                n = 5
                writefile.write(column[n][68:] + " ")
                n = 6
                while "source" not in column[n]:
                    writefile.write(column[n] + " ")
                    n += 1
                writefile.write("\n")
    searchfile.close()
    writefile.close()

sort_function("Trump")
print "Trump Complete"

sort_function("Bernie")
print "Bernie Complete"

sort_function("Cruz")
print "Cruz Complete"

sort_function("Kasich")
print "Kasich Complete"



