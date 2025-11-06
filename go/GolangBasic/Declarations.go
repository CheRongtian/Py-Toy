package main

import "fmt"

func main() {
	var foo int // declaration without initialization
	var bar int = 42 // declaration with initialization
	var x, y int = 42, 100 // multiple declaration and initialization at once
	var boo = 42 // go will judge and assign the type automatically
	//foo:= 42 same as above, could be used only in function
	const constant = "This is a constant"

	// go do not allowed declared variables to be not used
	_ = foo
	_ = bar
	_ = x
	_ = y
	_ = boo

	// iota can be used for incrementing numbers, starting from 0
	const (
		_ = iota // jump 0
		a
		b
		c = 1 << iota // bitwise left shift 3
		d // flow the upper method in const
	)
	fmt.Println(a, b) // 1 2 (0 is skipped)
	fmt.Println(c, d) // 8 16 (2^3 2^4)
}