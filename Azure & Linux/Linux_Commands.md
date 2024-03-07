

# What is Linux?

Open Source OS, it's a clone of UNIX, very reliable and customisable

## Linux Commands for navigating files and folders

 *  ls = lists files in the directory you're in
 *  ls -a = lists hidden files in the directory you're in
 *  pwd = (Present Working Directory) Show's you what directory you're currently in
 *  exit = to exit a session/log out
 *  cat /etc/shells = Shows what other shells there are available on Linux
 *  history = Shows the history of all the commands you've performed in a session in list format
 *  ls -l = Show's list of files as well as more details like permissions etc.
 *  ls -la = Show's list of files (including hidden) as well as more details like permissions etc.
 *  curl = Used for transferring data to/from a server using HTTP etc for use in downloading and uploading fies and more
 *  file = followed by a specific file name reveals the type of file by examining contents, unlike windows it doesn't judge off just file extension
 *  cp = followed by a file name copies the file, you then enter the copies new location
 *  mv = Used to both move a file (when followed by file name and then new location) OR can be used to rename a file by entering the file name and then the name you want to replace it with
 *  rm = deletes a file, but cannot delete a whole directory (folder)
 * --help = Shows a list of helpful commands/instructions on details about commands or commands performed
 *  rm -r (recursive) - will delete directory and all contents _DANGEROUS_
 * mkdir = (Make Directory), creaes a new folder(directory) 
 * cd = (Change Directory) followed by a directory name will move you to that particular directory but alone will return you to the home directory
 * .. = means the parent directory
 * . = means the current path
 * touch = used to make a new file
 * nano = Used to open and edit a particular file in a notepad style editor within the command line 
 * cat = mostly used for viewing contents of files but can be used in conjunction with other commands for more complex tasks
 * head = Head followed by -(any number) will show you the top lines up to the number entered
 * tail = tail followed by -(any number) will show you the bottom lines up to the number entered 
 * nl = makes lists numbered
 * cat <filename> | grep "word" = show lines containing a particular word/command/phrase with it highlighted
 * | = piping used to get the output from one command and give it to another command
 * sudo = (Superuser Do) gives you all permissions of super user
 * sudo apt install = Uses Sudo permissions to install something
 * sudo apt update -y = Searches for available updates
 * sudo apt upgrade -y = performs those updates/upgrades but requires input from user to do so
 * sudo su = logs you in as being root user temporarily
 * cd/ = changes to root directory
 * mv <folder/filename> . = moves file straight to home directory
 * mkdir <foldername>  <foldername> = will make multple folders at once
 * \ = used instead of spaces
 * treev = will display list of folders/files but in the form of a tree so you can see what is stored where
 * history -C = Clears history of commands from that session
 * ~ = tells us we're in the home directory
 * ps p$$ = Tells you the process you are using
 * ! (number of command) = will perform the command associated with the number you've chosen from the history list

## Scripting in Linux

### Nginx Installation

*Plan out a script before you make it to run...*

1. Ensure that you are using bash script using = #!/bin/bash
2. "sudo apt install nginx -y" - to install nginx
3. "sudo systemctl status nginx" - checks whether it has been installed 
4. You can check it's running in your browser by copying the VM's public IP address - when pasted into browser you should see the message "Welcome to nginx!"
5. "sudo systmctl is-enabled nginx" checks that it's been enabled
6. "chmod +x prov-nginx.sh" to enter change mode and execute the change

## Environment Variables

* printenv = prints all environment variables 
* printenv NAME OF VAR = prints only specififed variable
* echo = to print a variable to the screen with $$ in front
* VARIABLE=NAME = to name a variable
* export VARIABLE=NAME = in order to make that variable appear in the list
* source .bashrc = to reload a configuration into a session immediately


