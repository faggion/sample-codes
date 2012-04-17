# coding: utf-8
import os, logging, hashlib, hmac
import eventregist

class Base:
    @classmethod
    def encode(self, cls, arr):
        if not hasattr(cls, "separator1"):
            cls.separator1 = ":"
        if not hasattr(cls, "separator2"):
            cls.separator2 = ";"
        if not hasattr(cls, "version"):
            cls.version = 1.0
        if not hasattr(cls, "secret"):
            return None
        if cls.separator1 == cls.separator2:
            return None
        
        v = cls.separator2.join([unicode(cls.version)] + [unicode(x) for x in arr])
        sig = hmac.new(cls.secret, digestmod=hashlib.sha1)
        sig.update(v.encode("utf-8"))
        return "%s%s%s" % (sig.hexdigest(), cls.separator1, v)

    @classmethod
    def decode(self, cls, rawstr):
        if isinstance(rawstr, str):
            rawstr = rawstr.decode('utf-8')
        if not isinstance(rawstr, unicode):
            return None

        params = rawstr.split(cls.separator1,1)
        if len(params) != 2:
            return None

        body = params[1]
        hash = hmac.new(cls.secret, digestmod=hashlib.sha1)
        hash.update(body.encode("utf-8"))
        if hash.hexdigest() != params[0]:
            return None
        data = params[1].split(cls.separator2)
        return [float(data[0])] + data[1:]

class Access(Base):
    separator1 = "-"
    separator2 = "/"
    secret     = eventregist.config.get("access_token","secret")
    version    = float(eventregist.config.get("access_token","version"))
    keys       = eventregist.config.get("access_token","keys").split(",")

    @classmethod
    def encode(cls, data):
        arr = []
        for k in cls.keys:
            arr.append(unicode(data.get(k, "")))
        return Base.encode(cls, arr)
    @classmethod
    def decode(cls, rawstr):
        ret = {}
        arr = Base.decode(cls, rawstr)
        if arr[0] < cls.version:
            return None
        for i in range(1, len(arr)):
            ret[cls.keys[i-1]] = arr[i]
        return ret


