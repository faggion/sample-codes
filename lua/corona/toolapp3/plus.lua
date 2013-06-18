local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil

local function goHome(event)
   if event.phase == "ended" then
      storyboard.gotoScene("requests")
   end
end

function scene:createScene( event )
   local group = self.view
end

local function onRowRender(event)
   local fontSize = 18
   local label = display.newText(event.row, event.row.id, 10, 5, nil, fontSize)
   label:setTextColor( 0, 0, 0 )

   local rect = display.newRoundedRect(event.row, 10, fontSize + 15,
                                       display.contentWidth - 20,
                                       event.row.contentHeight - fontSize - 20 + 2,
                                       3)
   rect:setFillColor(230, 230, 230)
   rect.strokeWidth = 1
   rect:setStrokeColor(192, 192, 192)

   local value = display.newText(event.row, 'AAAAAbbb',
                                 15, fontSize + 18,
                                 display.contentWidth - 25,
                                 event.row.contentHeight - fontSize - 20,
                                 fontSize)
   value:setTextColor( 64, 64, 64 )

end

function scene:enterScene( event )
   local group = self.view

   -- middle contents
   tableView = widget.newTableView
   {
      top    = 70,
      width  = display.contentWidth,
      height = display.contentHeight - 50,
      noLines = true,
      hideScrollBar = false,
      bottomPadding = 80,
      onRowRender = onRowRender,
      --onRowTouch = onRowTouch,
   }
   group:insert( tableView )
   tableView:insertRow({id="label",   rowHeight=70})
   tableView:insertRow({id="url",     rowHeight=70})
   tableView:insertRow({id="method",  rowHeight=70})
   tableView:insertRow({id="body",    rowHeight=160})
   tableView:insertRow({id="headers", rowHeight=160})

   -- top title bar
   local title_bg = display.newRect(0, 0, display.contentWidth, 70)
   title_bg:setFillColor(32, 32, 32)
   group:insert(title_bg)
   local TITLE_HEIGHT = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Plus", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2 + 20
   group:insert(title)
   local btn_home = widget.newButton
   {
      left   = 10,
      top    = (TITLE_HEIGHT - TITLE_ICON_SIDE )/ 2 + 20,
      width  = TITLE_ICON_SIDE,
      height = TITLE_ICON_SIDE,
      defaultFile = "imgs/home.png",
      overFile    = "imgs/home.png",
      onEvent = goHome,
   }
   group:insert(btn_home)

   --nlocal desc = display.newText("This is Text.\nFoo\n  Bar", 20, 100, 280, 100, nil, 14 )
   --group:insert(desc)
end

function scene:exitScene( event )
   local group = self.view
end

function scene:destroyScene( event )
   local group = self.view
end

scene:addEventListener( "createScene",  scene )
scene:addEventListener( "enterScene",   scene )
scene:addEventListener( "exitScene",    scene )
scene:addEventListener( "destroyScene", scene )

return scene
