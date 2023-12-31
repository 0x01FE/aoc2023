package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type ConversionRange struct {
	source_start int
	source_end   int
	target_start int
	target_end   int
	translate    int
}

func convert(c *ConversionRange, num int) int {
	if num >= c.source_start && num <= c.source_end {
		return num + c.translate
	} else {
		return -1
	}
}

func print(c ConversionRange) {
	fmt.Println()
}

func main() {
	file, _ := os.Open("./test.text")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var seed_to_soil []*ConversionRange

	// Parse file
	index := 0
	s_to_s_mapping := false
	for scanner.Scan() {
		line := scanner.Text()

		// Get starting seeds

		if index == 0 {
			seeds_list := strings.Split(line, ": ")[1]
			seeds_value_list := strings.Split(seeds_list, " ")

			var seeds []int

			for _, seed := range seeds_value_list {
				seed_value, _ := strconv.Atoi(seed)
				seeds = append(seeds, seed_value)
			}

			fmt.Println("Seeds: ", seeds)
		}

		if line == "seed-to-soil map:" {
			s_to_s_mapping = true
			continue
		}

		if s_to_s_mapping {
			if line == "" {
				s_to_s_mapping = false
				for _, r := range seed_to_soil {
					print(r)
				}
				continue
			} else {
				var r_values []int
				range_strings := strings.Split(line, " ")
				for _, r := range range_strings {
					r_value, _ := strconv.Atoi(r)
					r_values = append(r_values, r_value)
				}

				var temp *ConversionRange
				temp = new(ConversionRange)

				temp.target_start = r_values[0]
				temp.source_start = r_values[1]
				length := r_values[2]

				temp.target_end = temp.target_start + length
				temp.source_end = temp.source_start + length
				temp.translate = temp.target_start - temp.target_end

				seed_to_soil = append(seed_to_soil, temp)
			}
		}

		index++
	}

}
