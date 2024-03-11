# Managing File Permissions

### Does being the owner of a file mean you have full permissions on that file? 

* Not always, there are cases where the owner may not have full permissions, such as when restricted by administrators or if a file has specific restrictions imposed. In most cases, however, the owner will have full permissions and can read, write, change permissions, delete contents etc. 

### If you give permissions to the User entity, what does this mean?

* This is like granting special access rights to the user who owns the file, these might be reading, writing or executing and will therefore dictate what a user can perform.

### If you give permissions to the Group entity, what does this mean?

* By giving permissions to the Group entity you're granting specific rights to a group of users that have common permissions that belong in the same group as the file. 

### If you give permissions to the Other entity, what does this mean?
* This is when you grant specific access rights to all users that are not the owner aren't associated with groups from the file. 

### Scenario:

*You give the following permissions to a file: User permissions are read-only, Group permissions are read and write, Other permissions are read, write, and execute. You are logged in as the user who is the owner of the file. What permissions will you have on this file?*

As the owner you'll only have _Read_ _Only_ permissions (--r) this is because the user permissions are read only, in summary, you can only view the files contents and not modify it or execute it.

### What can we gather from the permissions in this 'ls -l'?

-rwxr-xr-- 1 tcboony staff  123 Nov 25 18:36 keeprunning.sh

1. The 1st part of the line says 'rwx' which mean the User permissions are "Read, write and Execute"
2. The 2nd part of the line 'r-x' is the Group permissions section which give 'Execute and Read' permissions
3. The 3rd part 'r--' means other permissions are 'read only'
4. The 1 stands for one link in the file
5. 'tcboony' is the owner of the file
6. 'staff' is then the group associated with the file
7. The file's size is '123' bytes
8. The latest modification wasn on 'Nov 25' at "18:36"
9. the file name is 'keeprunning.sh'