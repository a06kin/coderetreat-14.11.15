package main

import "fmt"

var size = 3;
var twoD [3][3]byte;

func main() {
	twoD[0][1] = '*';

	vericalWorker(twoD, 0)

	for j := 1; j < size; j++{
		println("test");
		go vericalWorker(twoD, j)
	}

	fmt.Println(twoD)
	// TODO: read file
}

func vericalWorker(twoD [3][3]byte, i int){ 
	for j := 0; j < size; j++{
		println("vericalWorkerFor");
		fmt.Println(twoD[i][j])
		if(twoD[i][j] == byte('*')){
			println("vericalWorkerForIf");
			//TODO: if borders && if '*'
			twoD[i][j - 1]++
			twoD[i][j + 1]++
		}
	}
}

func corizontalWorker(twoD [3][3]byte, j int){ 
	println("corizontalWorker")
	for i := 0; i < size - 1; i++{
		if(twoD[i][j] == '*'){
			//TODO: if borders && if '*'
			twoD[i + 1][j]++
			twoD[i - 1][j]++
		}
	}
}