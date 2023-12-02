package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("./input.text")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	sum := 0

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ":")

		draws := strings.Split(line[1], ";")

		max_red := 0
		max_green := 0
		max_blue := 0

		for _, draw := range draws {

			cubes := strings.Split(draw, ",")
			for _, cube := range cubes {
				v := strings.Fields(cube)
				value, _ := strconv.Atoi(v[0])
				color := v[1]

				if color == "red" && value > max_red {
					max_red = value
				}
				if color == "green" && value > max_green {
					max_green = value
				}
				if color == "blue" && value > max_blue {
					max_blue = value
				}
			}
		}

		sum += max_red * max_green * max_blue
	}

	fmt.Println("Sum of the minimum power of all games:", sum)
}
