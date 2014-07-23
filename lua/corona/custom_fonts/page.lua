local storyboard = require("storyboard")
local page = {}

function page:new(g, n, t)
   local p   = {}
   p.next_scene = n
   p.texts   = t
   p.cursor  = 1
   p.frame   = nil
   p.content = nil
   p.group   = g
   local ret = setmetatable(p, {__index = page})
   ret:init(g)
   return ret
end

function page:init()
   self.frame = display.newRoundedRect(self.group, 
                                       display.contentWidth / 2,
                                       display.contentHeight - (180-5)/2,
                                       display.contentWidth - 6,
                                       180 - 10,
                                       5)
   self.frame:setFillColor(0.2, 0.2, 0.2)
   self.frame.setStrokeColor = {0.3,0,0}
   self.frame.strokeWidth = 3

   local message = ""
   if self.texts[self.cursor] then
      message = self.texts[self.cursor]
   end
   
   self.content = display.newText(self.group, message,
                                  display.contentWidth/2,
                                  display.contentHeight - (180-5)/2,
                                  display.contentWidth - 20,
                                  180 - 20,
                                  "PixelMplus10-Regular",
                                  20)
   self.content:setFillColor(0.8,0.8,0.8)

   Runtime:addEventListener("touch",
                            function(event) if ( event.phase == "ended" ) then self:next(); end end)
end

function page:next()
   if self.texts[self.cursor+1] then
      self.content.text = self.texts[self.cursor+1]
      self.cursor = self.cursor + 1
   else
      storyboard.gotoScene(self.next_scene)
   end
end

return page