import multiprocessing
import time
#square function
def square(x):
    return x*x
if __name__=='__main__':
    # multiproccessing pool object
    pool = multiprocessing.Pool()
    pool =multiprocessing.Pool(processes=4)
    inputs =[0,1,2,3,4]
    outputs=pool.map(square,inputs)
    print("input:{}".format(inputs))
    print("output: {}".format(outputs))
