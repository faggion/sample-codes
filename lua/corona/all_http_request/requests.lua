local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"

function scene:createScene( event )
   local group = self.view
   print("create scene2")
end

local function onRowRender(event)
   local label = display.newText( event.row, event.row.id, 0, 0, nil, 14)
   label.x = event.row.x - ( event.row.contentWidth * 0.5 ) + ( label.contentWidth * 0.5 ) + 10
   label.y = event.row.contentHeight / 2 - 10
   label:setTextColor( 0, 0, 0 )

   local exec_date = display.newText( event.row, "last executed: 2013/05/31 12:00:00", 0,0,nil,10)
   exec_date.x = event.row.x - ( event.row.contentWidth/2 ) + ( exec_date.contentWidth/2 ) + 10
   exec_date.y = event.row.contentHeight / 2 + 10
   exec_date:setTextColor( 0, 0, 0, 128 )
end

local function onRowTouch(event)

   if event.phase == 'release' then
      print('pressed')
      storyboard.gotoScene("detail")
   end
end

function scene:enterScene( event )
   local group = self.view

   -- top title bar
   local TITLE_HEIGHT = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Requests", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2
   group:insert(title)
   local plus_button = widget.newButton
   {
      left   = display.contentWidth - TITLE_ICON_SIDE - 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/plus.png",
      overFile    = "imgs/plus.png",
      onEvent = function() print("plus!"); end
   }
   group:insert(plus_button)

   -- middle contents
   local tableView = widget.newTableView
   {
      top    = 50,
      width  = 320, 
      height = display.contentHeight - 50,
      onRowRender = onRowRender,
      onRowTouch = onRowTouch,
   }
   group:insert( tableView )
   tableView:insertRow({isCategory=false,
                        id="request to my server 1",
                        rowHeight=50})
   tableView:insertRow({isCategory=false,
                        id="request to my server 2",
                        rowHeight=50})
   tableView:insertRow({isCategory=false,
                        id="request to my server 3",
                        rowHeight=50})

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
