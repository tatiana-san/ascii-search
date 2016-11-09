import StringIO

#This programme searchs custom string and returns the next n bytes after the first occurance

cfile=open("1.pdf", "rb")
data=cfile.read()
cfile.close()

data_decoded = str(data.decode('ascii', errors='ignore'))
n=500 #number of bytes to print

word=raw_input("Enter the key word: ")

while (True):  
    if word in data_decoded:
        print "Number of occurances: ", data_decoded.count(word), "\n"
        previous_index=0
        for i in range(0, data_decoded.count(word)):
            current_index=data_decoded.find(word, previous_index, len(data_decoded))
            print "Occurance", i+1, "( starts at byte #", current_index,"):\n"
            print data_decoded[current_index:current_index+n]
            print "------------------------------"
            previous_index=current_index+1     
    else:
        print "not found...\n\n"
    word=raw_input("Enter the key word: ")
