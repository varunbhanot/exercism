// Package hamming implements a solution for calculation hamming distance
package hamming

import (
	"errors"
)

// Distance returns hamming distance between 2 DNA strands input as string
func Distance(a, b string) (int, error) {
	var err error
	var result int
	if len(a) != len(b) {
		err = errors.New("String lengths not equal")
	} else {
		for index := 0; index < len(a); index++ {
			if a[index] != b[index] {
				result++
			}
		}
	}

	return result, err
}
