package main

import "fmt"

func main() {
	sa := []int{1, 2, 3, 4, 5}
	sb := sa[:3]
	fmt.Println(sa)
	fmt.Println(sb)

	sb[0] = 10
	fmt.Println(sa)
	fmt.Println(sb)
}
