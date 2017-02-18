import StringIO

#This programme searchs custom string and returns the next n bytes after the first occurance

cfile=open("1.pdf", "rb")
data=cfile.read() #read the data from file
cfile.close()

data_decoded = str(data.decode('ascii', errors='ignore')) #create an ASCII string with the data from file
n=500 #number of bytes to print

word=raw_input("Enter the key word: ") #enter the word you'd like to find in the file

while (True):   #User is asked (in loop) to enter a search word. If it is in the file, the number of occurances is returned
                #along with the first n symbols after each occurance (in list). If not - "not found..." 
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
