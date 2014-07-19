-- TODO: animation

local storyboard = require( "storyboard" )
local scene = storyboard.newScene()

function scene:createScene( event )
end

function scene:enterScene( event )
   local group = self.view
   print("enter scene1")

   local DISPLAY_WIDTH  = display.contentWidth
   local DISPLAY_HEIGHT = display.contentHeight
   local TITLE = {
      text="日本語も表示される",
      font={
         size=30,
         --family=native.systemFont,
         family="PixelMplus10-Regular",
      }
   }

   -- display scale values
   local bg = display.newRect(group,DISPLAY_WIDTH/2,
                              DISPLAY_HEIGHT/2,
                              DISPLAY_WIDTH,
                              DISPLAY_HEIGHT)
   bg:setFillColor(0.1,0.1,0.1)
   --group:insert(bg)

   local title = display.newText("", 0, 0,
                                 TITLE.font.family,
                                 TITLE.font.size)
   --title.isVisible = false
   title.text = TITLE.text
   -- object中心の位置がx,y (左上ではない)
   title.x = DISPLAY_WIDTH/2
   title.y = DISPLAY_HEIGHT/2 + 10
   title:setFillColor(0.8,0.8,0.8)

   --title.isVisible = true
   --group:insert(title)

   --timer.performWithDelay(500, function() storyboard.gotoScene("requests"); end )
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