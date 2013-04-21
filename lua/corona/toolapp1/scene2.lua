local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tab = require "tab"

function scene:createScene( event )
   local group = self.view
   print("create scene2")
end

local function onRowRender(event)
   local label = display.newText( event.row, "Row: " .. event.row.index, 0, 0, nil, 14 )
   label.x = event.row.x - ( event.row.contentWidth * 0.5 ) + ( label.contentWidth * 0.5 )
   label.y = event.row.contentHeight * 0.5
   label:setTextColor( 0, 0, 0 )
end

function scene:enterScene( event )
   local group = self.view

   local tableView = widget.newTableView
   {
      top    = 0,
      width  = 320, 
      height = 100,
      --maskFile = "assets/mask-320x366.png",
      --listener = tableViewListener,
      onRowRender = onRowRender,
      --onRowTouch = onRowTouch,
   }
   group:insert( tableView )
   tableView:insertRow({isCategory=false, rowHeight=50})
   tableView:insertRow({isCategory=false, rowHeight=50})
   tableView:insertRow({isCategory=false, rowHeight=50})
   tableView:insertRow({isCategory=false, rowHeight=50})
   tableView:insertRow({isCategory=false, rowHeight=50})


   local tabBar = widget.newTabBar(tab)
   tabBar:setSelected(2)
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
