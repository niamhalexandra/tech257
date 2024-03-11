# Linux Processes

## What are they?
Processes in Linux are when something being processed by the CPU, it doesn't necessarily need the CPU to be doing it but it's sitting in memory.

You may have many running concurrently (at the same time) but if there's only one core in the cpu it can only actually do one thing/run one process, but it switches between what needs cpu power, and it switches SO quickly that it's as if it is doing simultaneously.

Every process gets an ID (PID) so you can distinguish between processes.

TTY = the terminal sessions it's associated with, there's a little code given to your terminal at the start of a session. Processes with 'ps' are associated with you the user.

You can have parent processes which then creates a child process… you could kill a parent process by accident and If there's a child process still runnning in memory it is then referred to as a 'zombie process'. These can't be controlled… they won't necessarily do harm but just waste memory.

### Scenario's where you might kill a process:
* If an apps gone wrong and you just can't shut it down 
* On this course we may need to kill the parent process of "PM2" (process manager) this is a way to manage the node.js app we'd be running in the background, if you wanted to kill this app/process and PM2 was in process, it would spin it back up again so you'd go to PM2 to kill it rather than the app directly, if you did a brut force kill to PM2 the app would be a zombie process so you wouldn't really opt for that 

## So what does killing a process involve?

There are 64 levels of kill, 'kill' alone defaults to terminate gracefully, meaning the child process and parent process are both killed so no zombies, it's like medium force.

There is a stronger kill *Brut* *force* *kill* which is a last resort, so if can't use kill (which is actually -15 but you don't need the number) you'd have to use "kill-9" which when execusted  says 'killed' instead of 'terminated'. kill -1 is the most mild kill.

## Commands for use in Processes:
* Ps = lists processes associated with user
* Ps - e = lists all processes
* Ps -A = lists all processes
* Ps  aux = more details on processes can see the id
* Shift M = ranked by usage (is it taking all your memory)
* Shift P  = for processor, getting back to CPU 
* q= quit
* Sleep = specified for how long puts terminal to sleep for however long… number is in seconds, can use it for pauses in a script
Sleep (number) & = runs sleep in the background
Jobs= you can see processes in background?
Kill= end a process, got to make sure it's a process you know is ok to kill, that's why you need to know the id

