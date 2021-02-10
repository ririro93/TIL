# chmod (change access permissions)
This utility allows users to change the access permissions on files.
Examples:

 	chmod g+w   temp 	chmod g+rx  temp 	chmod go+rw temp 	chmod o-rw  temp 	chmod g-rwx temp 
This changes the access permissions of the file, "temp" to allow its group to write to it. Warning: Be careful with this command as it can cause you to remove access to your own files! Luckily you can use the same command to restore those permissions. This command basically allows you to specify who can do what to any file that you own.

See the above ls command description for more details on UNIX file permissions.

The access permission can be specified in the following format. The three parts of the format are given with no spaces between them.

[who] [operator] [permission]
- Who can be any combination of:
    - u :user (the file's owner).
    - g :group (the file's group members).
    - o :others (everyone else).
- Operator can be one of:
    - `+` :add the permissions to the file's existing set.
    - `-` :remove the given permissions from the file's set.
    - `=` :set the permissions to exactly this.
- Permission can be any combination of:
    - r :read permission.
    - w :write permission.
    - x :execute permission for programs.