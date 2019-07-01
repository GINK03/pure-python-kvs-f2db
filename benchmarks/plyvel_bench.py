from concurrent.futures import ProcessPoolExecutor as PPE
import plyvel
import time
import shutil
from collections import namedtuple
import pickle
import gzip
DATA = namedtuple('DATA', ['i', 'i_i', 'invi'])
shutil.rmtree('leveldb')
db = plyvel.DB('leveldb', create_if_missing=True)
start = time.time()

for i in range(100000):
    data = DATA(i=i, i_i=i*i, invi=1/(i+1))
    db.put(bytes(str(i), 'utf8'), gzip.compress(pickle.dumps(data)))

for i in range(100000):
    a = (i, pickle.loads(gzip.decompress(db.get(bytes(str(i), 'utf8')))))
end = time.time()
elapsed = end - start
db.close()
print(f'singlecore elapsed = {elapsed:0.06f}')

shutil.rmtree('leveldb')
db = plyvel.DB('leveldb', create_if_missing=True)
'''
not conflictiong test
'''
def pmap(arg):
    key, sargs = arg
    try:
        for i in sargs:
            data = DATA(i=i, i_i=i*i, invi=1/(i+1))
            db.put(bytes(str(i), 'utf8'), gzip.compress(pickle.dumps(data)))
        for i in sargs:
            a = (i, pickle.loads(gzip.decompress(db.get(bytes(str(i), 'utf8')))))
            #print(i, db.get(bytes(str(i), 'utf8')).decode())
    except exception as ex:
        print(ex)

# make_args
args = {}
for idx, i in enumerate(range(100_000)):
    key = idx % 16
    if args.get(key) is None:
        args[key] = []
    args[key].append(i)
args = [(key, sargs) for key, sargs in args.items()]

start = time.time()
with PPE(max_workers=16) as exe:
    exe.map(pmap, args)
end = time.time()
elapsed = end - start
err_count = 0
for i in range(100_000):
    try:
        i2, stores = (i*i, pickle.loads(gzip.decompress(db.get(bytes(str(i), 'utf8')))) )
    except Exception as ex:
        #print('there is expception', ex, i*i)
        err_count += 1
    #print(i, db.get(bytes(str(i), 'utf8')).decode())
db.close()
print(f'multicore no-confilict elapsed = {elapsed:0.06f}')
print('err rate', err_count/100_000)
