package = "tanarkypurelua"
version = "1.0-1"
source = {
   url = "http://tanarky.com/",
}
description = {
   summary = "An example for the LuaRocks tutorial.",
   detailed = [[
      This is an example for the LuaRocks tutorial.
      Here we would put a detailed, typically
      paragraph-long description.
   ]],
   homepage = "http://tanarky.com/",
   license = "MIT/X11",
}
dependencies = {
}
build = {
   type = "builtin",
   modules = {
      -- A simple module written in Lua
      hello = "src/hello.lua",
   }
}
