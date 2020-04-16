package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func MakeInputs(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	lines := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	inputs, _ := MakeInputs("day1input")

	sum := 0

	for i := 0; i < len(inputs); i++ {
		temp, _ := strconv.Atoi(inputs[i])
		temp = temp / 3
		temp = temp - 2

		sum = sum + temp

		for (temp/3 - 2) > 0 {
			temp = temp/3 - 2
			sum = sum + temp
		}
	}
	fmt.Println(sum)
}
