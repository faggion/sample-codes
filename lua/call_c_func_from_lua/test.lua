local m = require "cmsgpack"
local b = require "base64"

print("hello. it is OK.")

local tbl = { abc=123, foo=bar, hoge={xyz="hello, world", test=1.3, bl=true,none=nil}}
local tbl_bin = m.pack(tbl)

local tbl_bin_size = string.len(tbl_bin)
print("length is " .. tbl_bin_size)

func_binary(tbl_bin)

----local tbl_bin = cmsgpack.pack(tbl)
--
--local tbl_bin_size = string.len(tbl_bin)
--print("length is " .. tbl_bin_size)

--print(func_binary("\01\02\03\00\04\05"))

--print(func_binary(tbl_bin_size, bin))
--print(func_binary(bin))
--local tbl2 = cmsgpack.unpack((tbl_bin))
--local tbl2 = m.unpack((tbl_bin))
--print(tbl2.abc)
--print(tbl2.foo)
--print(tbl2.hoge.bl)
--print(tbl2.hoge.xyz)
--print(tbl2.hoge.test)
--print(tbl2.hoge.none)


--print(func_binary("hello"))
--print(func_addition(10, 20))
--print(func_addition(10, 20))
--print(func_open())
--print(func_open())
--print(func_open())
--print(func_close())
--print(func_close())
--print(func_close())