# Flash Friendly DB

このソフトウェアはフラッシュストレージに最適化されたPure PythonのKVSです。 
This software is Pure Python KVS optimized for flash storage.

## インストール/Install
Python 3.6以上が必要です。 
You need Python 3.6 or higher.  

```console
$ pip3 install f2db
```

## クイックスタート/Quick Start

```python
>>> import f2db
>>> db = f2db.f2db('f2db')
>>> db.save(key='foo', val=['bar', 1, 2, None, True])
>>> db.get('foo')
['bar', 1, 2, None, True]
```
keyはstr型、valはpythonのpickleでシリアライズできるオブジェクト型を受け付けることができます。  
Val can accept object types that can be serialized with pickle, key must to be str type.

## 特徴
 - 1. ファイルシステムベースのKVS/File system based KVS
 - 2. LevelDBやRocksDBに比べ並列アクセス、並列書き込みに強い(完全性は保証していない)/
Stronger in parallel access and parallel writing than LevelDB and RocksDB (completeness is not guaranteed)
 - 3. Pythonのオブジェクトをそのまま保存、復元できる/
You can save and restore Python objects as they are
