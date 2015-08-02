from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import sys
import time


def timex (st,f,x):
    print(st)
    start_time = time.time()
    tmp = f(x)
    print (tmp)
    print("--- %s seconds ---" % (time.time() - start_time))
    return tmp

def main (desti):
    merger = PdfFileMerger()
    dirs = sys.argv
    files = [x for x in os.listdir(dirs[1]) if x.endswith(".pdf")]
    for fname in sorted(files):
        merger.append(PdfFileReader(open (os.path.join(dirs[1], fname), 'rb')))
    merger.write(os.path.join(dirs[1],desti))
    print ("All content from directory %s has been merged into %s" % (dirs[1], desti))
    return "OK"

timex("Time elapsed : ", main, "output.pdf")
