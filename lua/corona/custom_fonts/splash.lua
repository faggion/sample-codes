-- TODO: animation

local storyboard = require("storyboard")
local page = require("page")
local scene = storyboard.newScene()
local DISPLAY_WIDTH  = display.contentWidth
local DISPLAY_HEIGHT = display.contentHeight

function scene:createScene( event )
end

function scene:enterScene( event )
   local group = self.view
   print("enter splash")

   -- display scale values
   local bg = display.newRect(group,DISPLAY_WIDTH/2,
                              DISPLAY_HEIGHT/2,
                              DISPLAY_WIDTH,
                              DISPLAY_HEIGHT)
   bg:setFillColor(0.1,0.1,0.1)

   local pg = page:new("scene_1",
                       {"こんにちは", "ようこそ"})

   -- map
   local options = {
      width = 32,
      height = 32,
      numFrames = 300,
      sheetContentWidth=640,
      sheetContentHeight=480
   }
   local map_tip = graphics.newImageSheet("img/map_tip.gif", options )
   local tile1 = display.newImage(group, map_tip, 3)
   tile1.x = 100
   tile1.y = 100

end

function scene:exitScene( event )
   local group = self.view
   print("exit splash")
end

function scene:destroyScene( event )
   local group = self.view
   print("destroy splash")
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene