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

		game_num, _ := strconv.Atoi(strings.Split(line[0], " ")[1])

		draws := strings.Split(line[1], ";")

		add := true

		for _, draw := range draws {

			cubes := strings.Split(draw, ",")
			for _, cube := range cubes {
				v := strings.Fields(cube)
				value, _ := strconv.Atoi(v[0])
				color := v[1]

				if color == "red" && value > 12 {
					add = false
				}
				if color == "green" && value > 13 {
					add = false
				}
				if color == "blue" && value > 14 {
					add = false
				}
			}
		}

		if add {
			sum += game_num
		}
	}

	fmt.Println("Sum of games with possible # of cubes:", sum)
}
