local storyboard = require( "storyboard" )
local scene = storyboard.newScene()

function scene:createScene( event )
end

function scene:enterScene( event )
   local group = self.view

   local icon_size   = 128
   local icon_pos_x  = (display.contentWidth - icon_size ) / 2
   local icon_margin = 5

   local icon_group = display.newGroup()
   for i=0,5 do
      local r1 = display.newRect( icon_pos_x , (icon_size + icon_margin) * i, icon_size, icon_size )
      r1:setFillColor(255, 166, 0)
      r1.tap = function(self, event) print("tapped: " .. i); end
      r1:addEventListener("tap")
      icon_group:insert(r1)
   end
   group:insert(icon_group)

   Runtime.touch = function(self, event)
      print("runtime touched: event.y=" .. event.y .. ", event.yStart=" .. event.yStart .. ", icon_group: icon_group.y=" .. icon_group.y )
      if event.phase == "began" then
         self.yInit = icon_group.y
      elseif event.phase == "moved" then
         icon_group.y = self.yInit - ( event.yStart - event.y )
      end
   end
   Runtime:addEventListener( "touch" )
end

function scene:exitScene( event )
   local group = self.view
   print("exit scene1")
end

function scene:destroyScene( event )
   local group = self.view
   print("destroy scene1")
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene