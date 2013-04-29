-- native.showWebPopup を使ったサンプル
-- request headerを指定できない＋httpレスポンスエラーコードをハンドリングできない

local http = require("socket.http")
local storyboard = require( "storyboard" )
local scene = storyboard.newScene()
local webView = nil
local remote_base = 'http://localhost:9999'

function scene:createScene( event )
   --local group = self.view
   local function listener( event )
      local shouldLoad = true
      local url = event.url
      print(url)
      print(event.errorCode)
      if 1 == string.find( url, remote_base .. "/help" ) then
         print("help page")
      elseif 1 == string.find( url, remote_base .. "/game" ) then
         print("game page")
      elseif 1 == string.find( url, remote_base .. "/" ) then
         print("top page")
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
      urlRequest=listener,
   }
   native.showWebPopup(0, 0, 320, 436, remote_base .. "/", options)
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