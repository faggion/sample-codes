local storyboard = require( "storyboard" )
local scene = storyboard.newScene()
function scene:createScene( event )
   local group = self.view
   print("hello scene1")
end

function scene:enterScene( event )
   local group = self.view
   print("enter scene1")
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