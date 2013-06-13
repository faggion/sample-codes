package main

import (
	"fmt"
//	"github.com/tanarky/string"
	"github.com/tanarky/rand"
)

func main() {
	//fmt.Println(string.Reverse(fmt.Sprintf("Hello, world; こんにちは、世界; %d", rand.Random())))

	for i:=0; i<3; i++ {
		rand.Seed(1)
		fmt.Println(fmt.Sprintf("rand: %d", rand.Random()))
	}
}
