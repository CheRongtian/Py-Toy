package main
import "fmt"

// a simple function
func functionName() {}

// function with parameters (again, types go after identifiers)
func functionName2(param1 string, param2 int){}

// multiple parameters of the same type
func functionName3(param1, param2 int){}

//return type declaration
func functionName4() int {
	return 42
}

// can return multiple values at once
func functionName5() (int, string) {
	return 42, "hello"
}

// return multiple named results simply by return
func functionName6() (n int, s string) {
	n = 42
	s = "foobar"
	// n and s will be returned
	return
}

func main() {
	var x, str = functionName5()
	var n, s = functionName6()
	
	fmt.Println(x, str)
	fmt.Println(n, s)
}