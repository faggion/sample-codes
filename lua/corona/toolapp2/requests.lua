local storyboard = require( "storyboard" )
local scene  = storyboard.newScene()
local widget = require "widget"
local tableView = nil

function scene:createScene( event )
   local group = self.view
end


local function onComplete( event )
--   if "clicked" == event.action then
--      local i = event.index
--      if 1 == i then
--         -- Do nothing; dialog will simply dismiss
--      end
--   end
end

local function treatInResponse(e)
   native.setActivityIndicator(false)

   local alert
   if e.isError then
      alert = native.showAlert( "Result",
                                "Error",
                                {"OK"},
                                onComplete)
   else
      alert = native.showAlert( "Result",
                                "IN request has been done successfully.",
                                {"OK"},
                                onComplete)
   end
end
local function treatOutResponse(e)
   native.setActivityIndicator(false)

   local alert
   if e.isError then
      alert = native.showAlert( "Result", "Error",
                                {"OK"}, onComplete)
   else
      alert = native.showAlert( "Result",
                                "OUT request has been done successfully.",
                                {"OK"},
                                onComplete)
   end
end
local function treatCurrentPointResponse(e)
   native.setActivityIndicator(false)

   local alert
   if e.isError then
      alert = native.showAlert( "Result", "Error",
                                {"OK"}, onComplete)
   else
      alert = native.showAlert( "Result",
                                e.response,
                                {"OK"},
                                onComplete)
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

local function sendInRequest(event)
   native.setActivityIndicator( true )

   local agent =
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; " ..
      ".NET CLR 1.1." .. math.random(1000, 9999) .. ")"

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

   local params = {}
   params.headers = headers
   network.request(url, "GET", treatInResponse, params)
end

local function sendOutRequest(event)
   native.setActivityIndicator( true )

   local agent =
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; " ..
      ".NET CLR 1.1." .. math.random(1000, 2000) .. ")"

   local headers = {}
   headers["User-Agent"] = agent
   headers["Referer"]    = "http://gourmet.blogmura.com/tokyogourmet/"
   headers["Cookie"]     = "click_cookie_id=" .. generate_click_cookie_id()

   local query = {
      ch  = "01023626",
      url = "http://mikan767676.appspot.com/",
   }
   url = 'http://link.blogmura.com/out/?' .. build_query(encode(query))

   local params = {}
   params.headers = headers
   network.request(url, "GET", treatOutResponse, params)
end

local function sendCurrentPointRequest(event)
   native.setActivityIndicator( true )

   local agent =
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; " ..
      ".NET CLR 1.1." .. math.random(1000, 2000) .. ")"

   local headers = {}
   headers["User-Agent"] = agent
   url = 'http://tanarky-test.appspot.com/point.html?output=rawtext'

   local params = {}
   params.headers = headers
   network.request(url, "GET", treatCurrentPointResponse, params)
end


local function onRowTouch(event)
   if event.phase == "release" then
      if event.row.id == 'in request' then
         sendInRequest(event)
      elseif event.row.id == 'out request' then
         sendOutRequest(event)
      else
         sendCurrentPointRequest(event)
      end
   end
end

function onRowRender(event)
   local label = display.newText( event.row, event.row.id, 0, 0, nil, 18)
   label.x = event.row.x - ( event.row.contentWidth/2 ) + ( label.contentWidth/2 ) + 10
   label.y = event.row.contentHeight / 2 - 2
   label:setTextColor( 0, 0, 0 )
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
   tableView:insertRow({id="in request",  height=50})
   tableView:insertRow({id="out request", height=50})
   tableView:insertRow({id="current point", height=50})

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
