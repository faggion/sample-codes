# coding: utf-8
from multiprocessing import Pool
import time

def f(x):
    #time.sleep(3)
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=4)              # 4つのワーカープロセスで開始
    result = pool.apply_async(f, [10])    # 非同期で "f(10)" を評価
    print result.get(timeout=1)           # あなたのコンピュータが *かなり* 遅くない限りは "100" を表示
    print pool.map(f, range(10))          # "[0, 1, 4,..., 81]" を表示
