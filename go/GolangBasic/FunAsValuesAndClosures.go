package main
import "fmt"


func main () {
	// assign a function to a name
	add := func(a, b int) int {
		return a + b
	}
	// use the name to call the function
	fmt.Println(add(3, 4))
	fmt.Println(scope()) // the first output is the address of the return function
	fmt.Println(scope()()) // the first () use scope(), the second () use the return value of scope()
 	fmt.Println(outer())
	infunc, val := outer()
	fmt.Println(infunc())
	fmt.Println(val)
}

// closures, lexically scoped: functions can access values that were
// in scope when defining the function
func scope() func() int{ // return a function that is a function with an int return
	outer_var := 2
	foo := func() int {return outer_var} // inner function can still visit the para for outer func even if outer func is stopped
	return foo
}

/*
func another_scope() func() int{
	// won't compile because outer_var and foo not defined in this scope
	outer_var = 444
	return foo
}
*/

// Closures
func outer() (func() int, int) {
	outer_var := 2
	inner := func() int {
		outer_var += 99 // outer_var from outer scope is mutated
		return outer_var
	}
	inner ()
	return inner, outer_var // return inner func and mutated outer_var 101
}