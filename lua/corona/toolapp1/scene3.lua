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

   tab:setSelectedButton(3)
   local tabBar = widget.newTabBar(tab)
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
