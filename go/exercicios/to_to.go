package main

import (
	"fmt"
	"encoding/json"
	"os"
)

func main(){
	menu()
 }

 type task struct{
	name	string	`json:"name"`
	doing	bool	`json:"doing"`
	done	bool	`json:"done"`
	toDo	bool	`json:"toDo"`
	status	string	`json:"status"`
}


 func menu(){
	var option int
	fmt.Printf("List taks press 1\n Create Task press 2\n Edit task press 3\n")

	switch option{
		case 1: ListTasks()
		case 2: CreateTask()
		case 3: EditTask()
	}
	
 }


 func Create(){
	var newTask task
	
	fmt.Printf("type task name: ")
	fmt.Scan(&newTask.name)

	fmt.Printf("type task status (to-do, doing, done): ")
	fmt.Scan(&newTask.status)

	if newTask.status == "to-do"{
		newTask.toDo = true
	}else if newTask.status == "doing"{
		newTask.doing = true
	}else if newTask.status == "done"{
		newTask.done = true
	}else{
		fmt.println("Invalid status.")
	}

	//saveToFile(newTask);
 }

 func saveToFile(taskToSave task){
	data, err := json.MarshalIndent(taskToSave, "", "	")
	if err != nil{
		fmt.Println("Errir encoding JSON: ", err)
		return
	}

	err = os.WriteFile("task.json", data, 0644)
	if err != nil{
		fmt.Println("Error while writing file: ", err)
		return
	}

	fmt.println("Task saved to file")
 }