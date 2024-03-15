# Using Numerics to Manage Permissions

## What numerics are assigned to each permission?

0 = no permissions at all

1 = is for Execute

2 =is for Write
   
4 = is for Read

## So what actions can be performed with each?

### Read and W

If you assign both read and write permissions, the numeric value would be the sum of the values for read and write permissions, which is 4 + 2 = 6.

Numeric Value for Read, Write, and Execute Permissions:
If you assign read, write, and execute permissions, the numeric value would be the sum of the values for read, write, and execute permissions, which is 4 + 2 + 1 = 7.

Numeric Value for Read and Execute Permissions:
If you assign read and execute permissions, the numeric value would be the sum of the values for read and execute permissions, which is 4 + 1 = 5.

Meaning of 644:
In the context of file permissions, the numeric value 644 represents the permissions assigned to a file. The first digit (6) represents the permissions for the owner of the file, the second digit (4) represents the permissions for the group associated with the file, and the third digit (4) represents the permissions for others. Specifically:

The owner has read and write permissions (6).
The group has read-only permissions (4).
Others have read-only permissions (4).
So, a file with permissions 644 would allow the owner to read and modify the file, while members of the group and others can only read the file.

GET A COMMAND EXAMPLE OF EXECUTE 644 permissions etc