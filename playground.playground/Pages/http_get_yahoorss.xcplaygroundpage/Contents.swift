//: [Previous](@previous)

import UIKit
import XCPlayground
XCPlaygroundPage.currentPage.needsIndefiniteExecution = true

var str = "Hello, playground"

print(str)

guard let feedUrl = NSURL(string: "http://rss.dailynews.yahoo.co.jp/fc/rss.xml") else { exit(1) }
print(feedUrl)

let session: NSURLSession = NSURLSession.sharedSession()
let request: NSMutableURLRequest = NSMutableURLRequest(URL: feedUrl)
request.HTTPMethod = "GET"
request.addValue("application/json", forHTTPHeaderField: "Accept")
session.dataTaskWithRequest(request, completionHandler: { data, response, error in
    if error == nil {
        print("OK")
        print(response)
        guard let xml = data else { exit(1) }
        print(String(data: xml, encoding: NSUTF8StringEncoding))
    }
    else {
        print("NG")
    }
    // code
}).resume()

