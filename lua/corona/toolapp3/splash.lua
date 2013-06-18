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
   local COLOR_THEME_1  = { r=12, g=160, b=208, a=255 }
   local TITLE = {
      text="All HTTP Request",
      font={
         size=30,
         family=native.systemFont,
      }
   }

   local bg = display.newRect(0, 20, DISPLAY_WIDTH, DISPLAY_HEIGHT)
   bg:setFillColor(COLOR_THEME_1.r,
                   COLOR_THEME_1.g,
                   COLOR_THEME_1.b,
                   COLOR_THEME_1.a)
   group:insert(bg)

   local title = display.newText("", 0, 0,
                                 TITLE.font.family,
                                 TITLE.font.size)
   --title.isVisible = false
   title.text = TITLE.text
   -- object中心の位置がx,y (左上ではない)
   title.x = DISPLAY_WIDTH/2
   title.y = DISPLAY_HEIGHT/2 + 10
   --title.isVisible = true
   group:insert(title)

   timer.performWithDelay(500, function() storyboard.gotoScene("requests"); end )
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