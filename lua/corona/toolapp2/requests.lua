local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil

function scene:createScene( event )
   local group = self.view
end


local function onComplete( event )
   if "clicked" == event.action then
      local i = event.index
      if 1 == i then
         -- Do nothing; dialog will simply dismiss
      end
   end
end

local function treatResponse(e)
   native.setActivityIndicator(false)

   local alert
   if e.isError then
      alert = native.showAlert( "Result", "Error",
                                {"OK"}, onComplete)
   else
      alert = native.showAlert( "Result", "Status = " .. e.status .. ", Date = " ..
                                e.responseHeaders.Date,
                                {"OK"}, onComplete)
   end

end

local function encode(t)
   ret = {}
   for k, v in pairs(t) do
      v = string.gsub (v, "\n", "")
      v = string.gsub (v, "([^0-9a-zA-Z ])",
                       function (c) return string.format ("%%%02X", string.byte(c)) end)
      v = string.gsub (v, " ", "+")
      ret[k] = v
   end
   return ret
end

local function build_query(q)
   local query = {}
   for k, v in pairs(q) do
      table.insert(query, k .. "=" .. v)
   end
   return table.concat(query, "&")
end

local function generate_click_cookie_id()
   local id = {}
   for i = 1, 16 do
      table.insert(id, math.random(1,9))
   end
   return table.concat(id, "")
end

local function onRowTouch(event)
   if event.phase == "release" then
      native.setActivityIndicator( true )

      local agent = 
         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; " ..
         ".NET CLR 1.1." .. math.random(1000, 2000) .. ")"

      local headers = {}
      headers["User-Agent"] = agent
      headers["Referer"]    = "http://gourmet.blogmura.com/tokyogourmet/"
      headers["Cookie"]     = "click_cookie_id=" .. generate_click_cookie_id()

      local query = {
         agent  = agent,
         ref    = "http://mikan767676.appspot.com/",
         newinp = "1",
         uri    = "http://gourmet.blogmura.com/tokyogourmet/"
      }
      query = encode(query)
      url = 'http://link.blogmura.com/link/c/000000?' .. build_query(query)
      --url = "http://localhost:9999/?" .. build_query(query)

      local params = {}
      params.headers = headers

      network.request(url, "GET", treatResponse, params)
      --timer.performWithDelay( 1000,
      --                        function() network.request(url, "GET", treatResponse, params);end,
      --                        1)
   end
end

function onRowRender(event)
   local label = display.newText( event.row, event.row.id, 0, 0, nil, 18)
   label.x = event.row.x - ( event.row.contentWidth/2 ) + ( label.contentWidth/2 ) + 10
   label.y = event.row.contentHeight / 2 - 2
   label:setTextColor( 0, 0, 0 )
   
   --local exec_date = display.newText( event.row, "last executed: 2013/05/31 12:00:00", 0,0,nil,10)
   --exec_date.x = event.row.x - ( event.row.contentWidth/2 ) + ( exec_date.contentWidth/2 ) + 50
   --exec_date.y = event.row.contentHeight / 2 + 8
   --exec_date:setTextColor( 0, 0, 0, 128 )
   --exec_date:addEventListener('touch', onRowTouch)
end

function scene:enterScene( event )
   local group = self.view

   -- middle contents
   tableView = widget.newTableView
   {
      top    = 70,
      width  = 320, 
      height = display.contentHeight - 50,
      onRowRender = onRowRender,
      onRowTouch = onRowTouch,
   }
   group:insert( tableView )
   tableView:insertRow({id="Do Request", height=50})
   --tableView:insertRow({id="request 2", height=50})

   -- top title bar
   local title_bg = display.newRect(0, 20, display.contentWidth, 50)
   title_bg:setFillColor(32, 32, 32)
   group:insert(title_bg)
   local TITLE_HEIGHT = 50
   local TITLE_ICON_SIDE = 30
   local title = display.newText("Requests", 0, 0, nil, 20 )
   title.x = display.contentWidth / 2 
   title.y = TITLE_HEIGHT / 2 + 20
   group:insert(title)

   if network.canDetectNetworkStatusChanges then
      network.setStatusListener( "www.apple.com", networkListener )
   else
      print("network reachability not supported on this platform")
   end

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
