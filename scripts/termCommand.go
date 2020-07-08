package main

import(
    "fmt"
    "log"
    "os/exec"
    "runtime"
    "time"
)

func runCommand() {
	cmd := exec.Command("python3.7", "getWanIp.py")
	if runtime.GOOS == "windows" {
		cmd = exec.Command("tasklist")
	}

	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	fmt.Printf("combined out:\n%s\n", string(out))
}

func main(){
    for t:= range time.NewTicker(10*time.Second).C{
        fmt.Println("Tick at: ",t)
        runCommand()
    }
}
