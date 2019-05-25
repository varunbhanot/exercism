
// Package  implements a solution for twofer exercise in exercism
package twofer

import (
	"fmt"
)
// checks the value of the name and return an expression according to its value
func ShareWith(name string) string {
	
	if name == "" {
		name = "you"
	}
	
	return fmt.Sprintf("One for %s, one for me.", name)
}
