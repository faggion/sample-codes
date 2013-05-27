local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil
local tfLabel = nil
local tfBody  = nil

function scene:createScene( event )
   local group = self.view
end

function scene:enterScene( event )
   local group = self.view

   -- top title bar
   local TITLE_HEIGHT = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Edit Basic Info", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2
   group:insert(title)
   local home_button = widget.newButton
   {
      left   = 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/home.png",
      overFile    = "imgs/home.png",
      onEvent = function() storyboard.gotoScene("requests"); end,
   }
   group:insert(home_button)

   -- BODY
   local ttLabel = display.newText( group, "Label", 10, 60, nil, 16)
   group:insert(ttLabel)
   tfLabel = native.newTextField( 30,
                                  90,
                                  display.contentWidth - 60,
                                  36 )
   tfLabel.font = native.newFont( native.systemFontBold, 24 )
   tfLabel.text = ""

   local ttMethod = display.newText( group, "Request Method", 10, 140, nil, 16)
   group:insert(ttMethod)
   local tfMethod = widget.newSegmentedControl
   {
      left = 30,
      top  = 180,
      segmentWidth = (display.contentWidth - 60)/4,
      height = 50,
      segments = { "GET", "POST", "PUT", "DELETE" },
      defaultSegment = 1,
   }
   group:insert(tfMethod)

   local ttBody = display.newText( group, "Request Body", 10, 220, nil, 16)
   group:insert(ttBody)
   tfBody = native.newTextBox( 30,
                               260,
                               display.contentWidth - 60,
                               150 )
   tfBody.font = native.newFont( native.systemFontBold, 14 )
   tfBody.text = "aaa\nbbb\nccc"
   tfBody.isEditable = true
   --tfBody.userInput = function() print("userinput"); end
   --tfBody:addEventListener("userInput")
   group:insert(tfBody)
   
   local submit = widget.newButton
   {
      left  = 0,
      top   = display.contentHeight - 50,
      width = display.contentWidth,
      height = 50,
      id = "button_1",
      label = "Submit",
      onRelease = function() print("OK"); end,
   }
   group:insert(submit)

end

function scene:exitScene( event )
   local group = self.view
   tfLabel:removeSelf()
   tfBody:removeSelf()
end

function scene:destroyScene( event )
   local group = self.view
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene
