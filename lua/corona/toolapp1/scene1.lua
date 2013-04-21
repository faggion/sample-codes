local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tab = require "tab"

function scene:createScene( event )
   local group = self.view
   print("create scene2")
end

function scene:enterScene( event )
   local group = self.view

   local myButton = widget.newButton
   {
      left    = 0,
      top     = 0,
      width   = 150,
      height  = 50,
      id      = "button1",
      label   = "my button",
      onEvent = function() print("ok"); end
   }
   group:insert(myButton)

   local pickerWheel = widget.newPickerWheel
   {
      top = 50,
      columns = { {width=100, align="right",  labels={"AAA", "BBB", "CCC"}},
                  {width=100, align="center", labels={"111", "222", "333"}}, },
   }
   group:insert(pickerWheel)

   local tabBar = widget.newTabBar(tab)
   tabBar:setSelected(1)
   group:insert(tabBar)
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