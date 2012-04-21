# coding: utf-8
import logging
import urllib2
import urllib
import json

def main():
    params = { "appid":"tanarky_devel",
               "query":"vaio"}
    url = "http://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?%s" % urllib.urlencode(params)
    request = urllib2.Request(url)
    #request.add_header('Host', 'localhost')
    #request.add_header('User-Agent', agent)
    #request.add_header('Referer', 'http://gourmet.blogmura.com/lunch/')
    #request.add_header('Cookie','click_cookie_id=%s;' % make_click_cookie_id())
    response = urllib2.urlopen(request)
    response_data = json.loads(response.read())
    #logging.debug(response_data["ResultSet"][0]["Result"][0]["Name"])
    #logging.debug(response_data["ResultSet"]["totalResultsAvailable"])
    #logging.debug(response_data["ResultSet"]["0"])
    logging.debug(response_data["ResultSet"]["0"]["Result"]["0"]["Name"])

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    main()
