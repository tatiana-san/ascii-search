import StringIO

#This programme searchs custom string and returns the next n bytes after the first occurance

cfile=open("1.pdf", "rb")
data=cfile.read()
cfile.close()

data_decoded = str(data.decode('ascii', errors='ignore'))
n=300 #number of bytes to print

word=raw_input("Enter the key word: ")

while (word!="endcode"):  
    if word in data_decoded:
        indexW=data_decoded.index(word)
        areaW=data_decoded[indexW:indexW+n]
        print "Index: ", indexW
        print "Next", n, "bytes:\n\n", areaW, "\n\n"
    else:
        print "not found...\n\n"
    word=raw_input("Enter the key word: ")
