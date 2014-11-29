// Playground - noun: a place where people can play

import UIKit

var imgurl = NSURL(string:"http://img.tiqav.com/1oM.jpg")
var data = NSData(contentsOfURL: imgurl!, options: nil, error: nil)
var image = UIImage(data:data!)


var num1 = 10
var num2 = 20

var rect = CGRect(x: num1, y: num2, width:100, height:100)
var label = UILabel(frame: rect)

var value = 1
for i in 1...10 {
    value += 1
}





