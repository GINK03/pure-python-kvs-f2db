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
>>> db.save(key='baz', val='2nd-value')
>>> list(db.get_iter())
['2nd-value', ['bar', 1, 2, None, True]]
```
keyはstr型、valはpythonのpickleでシリアライズできるオブジェクト型を受け付けることができます。  
Val can accept object types that can be serialized with pickle, key must to be str type.

## 特徴/Features
 - 1. ファイルシステムベースのKVS/File system based KVS
 - 2. LevelDBやRocksDBに比べ並列アクセス、並列書き込みに強い(完全性は保証していない)/
Stronger in parallel access and parallel writing than LevelDB and RocksDB (completeness is not guaranteed)
 - 3. Pythonのオブジェクトをそのまま保存、復元できる/
You can save and restore Python objects as they are

## ベンチマーク/Benchmark

<div align="center">
 <img width="500px" src="https://user-images.githubusercontent.com/4949982/60440147-23e3ec80-9c4f-11e9-8c79-66646b480555.png">
 <div> Fig. 1 </div>
</div>
並列での処理を考慮すると処理が重いとき、良好なパフォーマンスを発揮する  

Provides good performance when processing is heavy considering parallel processing  
