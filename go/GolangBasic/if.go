package main
import "fmt"

func main() {

	x := 5

	// basic one
	if x > 10{
		fmt.Println(x)
	} else if x == 10{
		fmt.Println(10)
	} else{
		fmt.Println(-x)
	}

	b := 10
	c := 12

	// you can put one statement before the condition
	if a := b + c; a < 42 {
		fmt.Println(a)
	} else {
		fmt.Println(a - 42)
	}

	// type assertion inside if
	var val interface{} = "foo" // put "foo"(any type) into the interface
	if str, ok := val.(string); ok{ 
		// if inside val is string, please take it as string; if it is, then ok: has output, else no output
		fmt.Println(str)
	}
}