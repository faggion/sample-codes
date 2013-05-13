local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"

function scene:createScene( event )
   local group = self.view
   print("create scene2")
end

function onPressHome(event)
   storyboard.gotoScene("requests")
end

function scene:enterScene( event )
   local group = self.view

   -- top title bar
   local TITLE_HEIGHT    = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Detail", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2
   group:insert(title)
   local back_button = widget.newButton
   {
      left   = 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/home.png",
      overFile    = "imgs/home.png",
      onEvent = onPressHome,
   }
   group:insert(back_button)
end

function scene:exitScene( event )
   local group = self.view
   print("exit scene2")
end

function scene:destroyScene( event )
   local group = self.view
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene