//: [Previous](@previous)

//import Foundation
import UIKit
import XCPlayground
XCPlaygroundPage.currentPage.needsIndefiniteExecution = true

var v = UIView(frame: CGRectMake(0, 0, 200, 200))

var button = UIButton(frame: CGRectMake(75, 0, 50, 50))
button.layer.cornerRadius = 10.0

button.setTitle("like", forState: UIControlState.Normal)
button.setTitleColor(UIColor.orangeColor(), forState: UIControlState.Normal)
button.backgroundColor = UIColor.blueColor()

var label1 = UILabel(frame: CGRectMake(75, 80, 100, 100))
label1.text = "hello"

v.addSubview(label1)
v.addSubview(button)


//: [Next](@next)
