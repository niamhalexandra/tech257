## Why is file ownership so important?

* *Security* - It determines who has access to files/directories, it means that admins can restrict access to any sensitive data and prevent certain people from modifying critical files
* *Accountability* - If an owner of a file can be identified it helps with tracking changes, debugging and enforcing compliance
*  *Control* - Admins are able to delegate responsibilities and manage access rights. They can control who reads,write or execute files/directories

### What command do we use to view file ownership?

You use command "ls -l" if you want to see just visible files but you can also use "ls -la" if you want to see details about any hidden files as well.

### What permissions are set when users create a file or directory & who does the file/directory belong to?

* Permissions are usually set to 'unmask value' which is something that specifies permissions that should be removed from newly created files/directories. By default files are created with the permissions: "rw-rw-r--"(644) and directories with "rwxrwxr-x"(755)
### Why do owners not receive X permissions when creating a file?
* Owners don't, by default, receive (X) permissions when they create files for security purposes. So instead of granting permission straight away you have to explicitly grant execution rights.

### What command is used to change the owner of a file?

chown [options] user:group file_or_directory
