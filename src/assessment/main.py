import csv
import multiprocessing as mp
from multiprocessing import Process, Queue
import sys
import click
import logging
import os, time

# Local imports

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))
from common.dummy_ai import getCompanyAttractiveness

# Logger definition
logging.basicConfig(format="%(message)s", level=logging.INFO)
@click.command()
def test():
    print("working fine")

@click.option(
    "--filename",
    default="/data/nasdaq-company-list.csv",
    help="Input CSV file name"
)
@click.option(
    "--top",
    default=50,
    help="Number of companies Symbols to print at the end"
)

def main(filepath, threads: int, top=10):
    symbols=[]
    mycsv= csv.reader(open(filepath))
    for row in mycsv:
        symbols.append(row[0])
    symbols.pop(0)
    start_time = time.time()
    pool = mp.Pool(threads)
    
    result = pool.map(getCompanyAttractiveness, symbols)
    print("time for processing: ",time.time()-start_time, "s")
    print (sorted (result, key= lambda k: k["score"],reverse=True)[:top])

    #logging.info(getCompanyAttractiveness("GOOGL"))
   
if __name__ == "__main__":
    main("../data/nasdaq-company-list.csv",threads=30,top=4)
