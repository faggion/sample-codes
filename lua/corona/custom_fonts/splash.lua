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

   -- map
   local options = {
      width = 32,
      height = 32,
      numFrames = 300,
      sheetContentWidth=640,
      sheetContentHeight=480
   }
   local map_tip = graphics.newImageSheet("img/map_tip.gif", options )
   local tile1
   for c = 1, 10 do
      for r = 1, 15 do
         tile1 = display.newImage(group, map_tip, 2)
         tile1.x = (c-1) * 32 + 16
         tile1.y = (r-1) * 32 + 16
      end
   end

   local pg = page:new(group, "scene_1",
                       {"こんにちは\nあああああああああああああああ\nあ\nあ\nあ\nあ", "ようこそ"})


   local person = display.newImage(group, "img/male.gif",  80, 80)

   --local options = {
   --   width = 64,
   --   height = 64,
   --   numFrames = 300,
   --   sheetContentWidth=1280,
   --   sheetContentHeight=960
   --}
   --local map_tip = graphics.newImageSheet("img/map_tip.gif", options )
   --local tile1
   --for c = 1, 5 do
   --   for r = 1, 7 do
   --      tile1 = display.newImage(group, map_tip, 2)
   --      tile1.x = (c-1) * 64 + 32
   --      tile1.y = (r-1) * 64 + 32
   --   end
   --end

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