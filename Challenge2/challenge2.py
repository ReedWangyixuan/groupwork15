import numpy as np
import pylab as pl

def get_data(lines):
    sizeArray=[]
    for line in lines:
        line = line.replace("\n","")
        diff = int(line)
        sizeArray.append(diff)
    return np.array(sizeArray)

def draw_hist(sizeArray):
    data = sizeArray
    for i in range(2,31):
        bins = np.linspace(min(data),max(data),i+1)
        pl.hist(data,bins)
        pl.xlabel("Time Diff")
        pl.ylabel("Frequency")
        pl.title("The Frequency of different Time Diff")
        #pl.savefig("bin=i.png")
        #pl.clf()
        pl.show()
        
if __name__ == "__main__":
    with open("D:\\大二下\\数据科学编程\\homework1\\only_diff_data_v4.4.csv") as f:
        #df.set_index(["lv"],inplace=True)
        lines = f.readlines()
    sizeArray = get_data(lines)
    draw_hist(sizeArray)


