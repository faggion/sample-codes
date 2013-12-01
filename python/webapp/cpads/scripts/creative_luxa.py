# coding: utf-8

import logging, requests, sys, os, traceback, json, datetime, time

url_adc = 'http://localhost:8080/a/adc'

def main(adv_name):
    creatives = [
        {"name": "%s-%d" % (adv_name, 31584),
         "tmpl_id": 1,
         "expire_at": int(time.time()) + 60*60*10,
         "lp": "https://luxa.jp/lx/deal/31584/",
         "img_url": "http://d2oe86l9d1xq1n.cloudfront.net/dynimg/4874/31584/L1_3F87CEDF72A849FEBBDA6C3F668905B2.jpg?v=1385837188735",
         "title": "【ZAGAT掲載】贅を尽くした邸宅レストランで過ごす幻想の一夜《和牛フィレ肉とフォアグラなど全8品のMenu Speciale dello Chef》数々の名店で研鑽を積んだシェフの正統派イタリアンを召し上がれ",
         "price": 9800,
         "org_price": 16500}
        ]
    for c in creatives:
        ret = requests.put(url_adc,
                           data=json.dumps({"advertiser": { "name": adv_name },
                                            "creative": c}),
                           headers={"content-type": "application/json"})
        logging.debug(ret.text)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    main(sys.argv[1])
