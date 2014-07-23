local storyboard = require("storyboard")
local tile = {}

function tile:new(img, opt)
   local p = {}
   p.img   = img
   p.opt   = opt
   local ret = setmetatable(p, {__index = tile})
   ret:init()
   return ret
end

function tile:init()
end

return tile
