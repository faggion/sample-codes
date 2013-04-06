local storyboard = require( "storyboard" )
local scene = storyboard.newScene()
local webView = nil

function scene:createScene( event )
   local group = self.view
   --webView = native.newWebView( 0, 0, 320, 480 )
   --webView:request( "http://www.coronalabs.com/" )
   --webView:request( "local.html" )
   --group:insert(webView)
   print("hello scene1")

   local function listener( event )
      local shouldLoad = true
      local url = event.url
      if 1 == string.find( url, "corona:close" ) then
         shouldLoad = false
      end
      if event.errorCode then
         print( "Error: " .. tostring( event.errorMessage ) )
         shouldLoad = false
      end
      return shouldLoad
   end
   local options = {
      hasBackground=true,
      baseUrl=system.ResourceDirectory,
      urlRequest=listener
   }
   native.showWebPopup(0, 0, 320, 436, "local.html", options)
   --native.showWebPopup(0, 0, 320, 436, "http://www.yahoo.co.jp/")
   
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
   webView:removeSelf()
   webView = nil
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene