local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil

local function plus(event)
   if event.phase == "ended" then
      storyboard.gotoScene("plus")
   end
end

function scene:createScene( event )
   local group = self.view
end

function scene:enterScene( event )
   local group = self.view

   -- top title bar
   local title_bg = display.newRect(0, 20, display.contentWidth, 50)
   title_bg:setFillColor(32, 32, 32)
   group:insert(title_bg)
   local TITLE_HEIGHT = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Requests", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2 + 20
   group:insert(title)
   local plus_button = widget.newButton
   {
      left   = display.contentWidth - TITLE_ICON_SIDE - 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2 + 20,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/plus.png",
      overFile    = "imgs/plus.png",
      onEvent = plus,
   }
   group:insert(plus_button)

   local desc = display.newText("This is Text.\nFoo\n  Bar", 20, 100, 280, 100, nil, 14 )
   group:insert(desc)
end

function scene:exitScene( event )
   local group = self.view
end

function scene:destroyScene( event )
   local group = self.view
end

scene:addEventListener( "createScene",  scene )
scene:addEventListener( "enterScene",   scene )
scene:addEventListener( "exitScene",    scene )
scene:addEventListener( "destroyScene", scene )

return scene
