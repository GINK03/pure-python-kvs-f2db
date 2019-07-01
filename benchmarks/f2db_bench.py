from concurrent.futures import ProcessPoolExecutor as PPE
import time
import shutil
import f2db
from collections import namedtuple
DATA = namedtuple('DATA', ['i', 'i_i', 'invi'])

try:
    shutil.rmtree('f2db')
except Exception as ex:
    ...
db = f2db.f2db(tar_path='f2db')

start = time.time()
for i in range(500000):
    db.save(key=str(i), val=DATA(i=i, i_i=i*i, invi=1/(i+1)))

for i in range(500000):
    a = (i, db.get(key=str(i)))
end = time.time()
elapsed = end - start
print(f'singlecore elapsed = {elapsed:0.06f}')
#exit()
'''
not conflictiong test
'''


def pmap(arg):
    key, sargs = arg
    try:
        for i in sargs:
            db.save(key=str(i), val=DATA(i=i, i_i=i*i, invi=1/(i+1)))
        for i in sargs:
            a = (i, db.get(key=str(i)))
    except exception as ex:
        print(ex)

del db
shutil.rmtree('f2db')
db = f2db.f2db(tar_path='f2db')
# make_args
args = {}
for idx, i in enumerate(range(500_000)):
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
for i in range(500_000):
    try:
        i2, data = (i*i, db.get(key=str(i)))
    except Exception as ex:
        #print('there is expception', ex, i*i)
        err_count += 1
print(f'multicore no-confilict elapsed = {elapsed:0.06f}')
print('err rate', err_count/100_000)
