package main
import "fmt"

func main(){
	/*
	bool strig 
	int  int8  int16  int32  int64 
	uint uint8 uint16 uint32 uint64 uintptr

	byte // alias for uint8
	rune // alias for int32 ~= a character(Unicode code point) - very Viking
	float32 float64
	complex64 complex128
	*/
	var i int = 42 // i := 42
	var f float64 = float64(i) // f := float(i)
	var u uint = uint(f) // u := uint(f)
	
	_ = i
	_ = f
	_ = u
}