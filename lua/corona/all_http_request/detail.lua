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
   local home_button = widget.newButton
   {
      left   = 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/home.png",
      overFile    = "imgs/home.png",
      onEvent = onPressHome,
   }
   group:insert(home_button)

   local bg_rect = display.newRect(0, 50, display.contentWidth, 50)
   bg_rect:setFillColor(50, 50, 50)
   group:insert(bg_rect)
   -- delete button
   local delete_button = widget.newButton
   {
      left   = (display.contentWidth - TITLE_ICON_SIDE)/ 2 - 90,
      top    = 60,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/delete.png",
      overFile    = "imgs/delete.png",
      onEvent = onPressHome,
   }
   group:insert(delete_button)
   -- edit button
   local edit_button = widget.newButton
   {
      left   = (display.contentWidth - TITLE_ICON_SIDE)/ 2 - 30,
      top    = 60,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/edit.png",
      overFile    = "imgs/edit.png",
      onEvent = onPressHome,
   }
   group:insert(edit_button)
   -- execute button
   local execute_button = widget.newButton
   {
      left   = (display.contentWidth - TITLE_ICON_SIDE)/ 2 + 30,
      top    = 60,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/execute.png",
      overFile    = "imgs/execute.png",
      onEvent = onPressHome,
   }
   group:insert(execute_button)
   -- copy button
   local copy_button = widget.newButton
   {
      left   = (display.contentWidth - TITLE_ICON_SIDE)/ 2 + 90,
      top    = 60,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/copy.png",
      overFile    = "imgs/copy.png",
      onEvent = onPressHome,
   }
   group:insert(copy_button)

   
   -- BODY
   local ROW_HEIGHT = 30
   local ROW_START  = 100
   local ROW_MARGIN = 10
   local t_label = display.newText("Label", 10, ROW_START+ROW_MARGIN+ROW_HEIGHT*0, nil, 16 )
   group:insert(t_label)
   local v_label = display.newText("This is hoge Request Label",
                                   30,
                                   ROW_START+ROW_MARGIN+ROW_HEIGHT*1,
                                   nil, 16 )
   group:insert(v_label)

   local t_url = display.newText("URL", 10,
                                 ROW_START+ROW_MARGIN+ROW_HEIGHT*2,
                                 nil, 16 )
   group:insert(t_url)
   local v_url = display.newText("http://example.com/api", 30,
                                 ROW_START+ROW_MARGIN+ROW_HEIGHT*3,
                                 nil, 16 )
   group:insert(v_url)

   local t_method = display.newText("Method", 10,
                                    ROW_START+ROW_MARGIN+ROW_HEIGHT*4,
                                    nil, 16 )
   group:insert(t_method)
   local v_method = display.newText("GET", 30,
                                    ROW_START+ROW_MARGIN+ROW_HEIGHT*5,
                                    nil, 16 )
   group:insert(v_method)

   local t_rqh = display.newText("Request Headers", 10, 
                                 ROW_START+ROW_MARGIN+ROW_HEIGHT*6,
                                 nil, 16 )
   group:insert(t_rqh)

   local t_rqh1 = display.newText("Content-type: application/json", 20,
                                  ROW_START+ROW_MARGIN+ROW_HEIGHT*7,
                                  nil, 16 )
   group:insert(t_rqh1)
   local t_rqh2 = display.newText("Coookie: foo=bar;hoge=fuga", 20,
                                  ROW_START+ROW_MARGIN+ROW_HEIGHT*8,
                                  nil, 16 )
   group:insert(t_rqh2)
   local t_rqh3 = display.newText("X-Foo: Bar", 20,
                                  ROW_START+ROW_MARGIN+ROW_HEIGHT*9,
                                  nil, 16 )
   group:insert(t_rqh3)

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