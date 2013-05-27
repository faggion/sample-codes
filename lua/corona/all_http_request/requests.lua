local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil

function scene:createScene( event )
   local group = self.view
   print("create scene2")
end

local function onRowTouch(event)
   if event.phase == "began" then
      storyboard.gotoScene("detail")
   end
end

local function Plus(event)
   if event.phase == "began" then
      storyboard.gotoScene("edit_basic")
   end
end

function onRowRender(event)
   local label = display.newText( event.row, event.row.id, 0, 0, nil, 14)
   label.x = event.row.x - ( event.row.contentWidth/2 ) + ( label.contentWidth/2 ) + 50
   label.y = event.row.contentHeight / 2 - 10
   label:setTextColor( 0, 0, 0 )
   label:addEventListener('touch', onRowTouch)
   
   local exec_date = display.newText( event.row, "last executed: 2013/05/31 12:00:00", 0,0,nil,10)
   exec_date.x = event.row.x - ( event.row.contentWidth/2 ) + ( exec_date.contentWidth/2 ) + 50
   exec_date.y = event.row.contentHeight / 2 + 8
   exec_date:setTextColor( 0, 0, 0, 128 )
   exec_date:addEventListener('touch', onRowTouch)
   
   local icon_exec = display.newImageRect(event.row, "imgs/execute.png", 30, 30)
   icon_exec.x = 25
   icon_exec.y = event.row.contentHeight / 2 - 8
   function icon_exec:touch(event)
      if event.phase == "began" then
         print('touch began')
      end
   end
   icon_exec:addEventListener('touch')
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
   local settings_button = widget.newButton
   {
      left   = 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/settings.png",
      overFile    = "imgs/settings.png",
      onEvent = function() print("goto settings page"); end,
   }
   group:insert(settings_button)
   local plus_button = widget.newButton
   {
      left   = display.contentWidth - TITLE_ICON_SIDE - 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/plus.png",
      overFile    = "imgs/plus.png",
      onEvent = Plus,
   }
   group:insert(plus_button)

   -- middle contents
   tableView = widget.newTableView
   {
      top    = 50,
      width  = 320, 
      height = display.contentHeight - 50,
      onRowRender = onRowRender,
      --onRowTouch = onRowTouch,
   }
   group:insert( tableView )
   tableView:insertRow({id="request to my server 1", height=50})
   tableView:insertRow({id="request to my server 2", height=50})

end

function scene:exitScene( event )
   local group = self.view
   print("exit requests.lua")
end

function scene:destroyScene( event )
   local group = self.view
   print("destroy requests.lua")
end

scene:addEventListener( "createScene", scene )
scene:addEventListener( "enterScene", scene )
scene:addEventListener( "exitScene", scene )
scene:addEventListener( "destroyScene", scene )

return scene
