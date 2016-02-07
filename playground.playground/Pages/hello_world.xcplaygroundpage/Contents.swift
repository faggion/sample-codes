// Playground - noun: a place where people can play

import UIKit

//other setup

let uiButton   = UIButton(type: UIButtonType.System) as UIButton
uiButton.frame  = CGRectMake(0, 0, 200, 200)
uiButton.setTitle("Test", forState: UIControlState.Normal);

var imgurl = NSURL(string:"http://img.tiqav.com/1oM.jpg")
var data = NSData(contentsOfURL: imgurl!)
var image = UIImage(data:data!)


var num1 = 10
var num2 = 20

var rect = CGRect(x: num1, y: num2, width:100, height:100)
var label = UILabel(frame: rect)

var value = 1
for i in 1...10 {
    value += 1
}





