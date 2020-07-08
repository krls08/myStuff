package main

import (
    "fmt"
    "os/exec"
    //"runtime"
)

func execute(){
    out,err := exec.Command("python","getWanIp.py").Output()

    if err != nil{
        fmt.Printf("%s",err)
    }

    fmt.Println("Command successfully executed")
    output := string(out[:])
    fmt.Println("command output:")
    fmt.Println(output)
    fmt.Println("End of command")

}

func main(){
    execute()
}
