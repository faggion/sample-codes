-- TODO: animation

local storyboard = require("storyboard")
require("message")
local scene = storyboard.newScene()
local DISPLAY_WIDTH  = display.contentWidth
local DISPLAY_HEIGHT = display.contentHeight

function scene:createScene( event )
end

function scene:enterScene( event )
   local group = self.view
   print("enter scene1")

   -- display scale values
   local bg = display.newRect(group,DISPLAY_WIDTH/2,
                              DISPLAY_HEIGHT/2,
                              DISPLAY_WIDTH,
                              DISPLAY_HEIGHT)
   bg:setFillColor(0,0,0.8)

   message.show("1行目です\nあいうえおかきくけこさしすせそ\nあ\nあ\nあ\nおわり")
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