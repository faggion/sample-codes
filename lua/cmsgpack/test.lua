local m = require "cmsgpack"
local b = require "base64"
print(b.encode("B"))

local bar = "dragon"
local tbl = { abc=123, foo=bar, hoge={xyz="hello, world", test=1.3, bl=true,none=nil}}
local tbl_bin = cmsgpack.pack(tbl) 
print("length is " .. string.len(tbl_bin))
print(b.encode(tbl_bin))
local tbl2 = cmsgpack.unpack((tbl_bin))
print(tbl2.abc)
print(tbl2.foo)
print(tbl2.hoge.bl)
print(tbl2.hoge.xyz)
print(tbl2.hoge.test)

