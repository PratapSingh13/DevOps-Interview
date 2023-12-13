# What is Soft Link And Hard Link In Linux?

A **soft link** is an actual link to the original file, whereas a **hard link** is a mirror copy of the original file. If you delete the original file, the soft link has no value, because it points to a non-existent file.

But in the case of hard link, it is entirely opposite. Even if you delete the original file, the hard link will still has the data of the original file. Because hard link acts as a mirror copy of the original file.

### **A soft link**
-   Allows you to link between directories
-   Has different inode number and file permissions than original file
-   Permissions will not be updated if we change the permissions of source file
-   Soft link has only the path of the original file, not the contents

### **A Hard link**
-   Can't link directories
-   Has the same inode number and permissions of original file
-   Permissions will be updated if we change the permissions of source file
-   Hard link has the actual contents of original file, so that you still can view the contents, even if the original file moved or removed.


## How to create Soft Link
Let us create an empty directory called "test"

```bash 
$ mkdir test
```

Change to the "test" directory:

```bash 
$ cd test
```

Now, create a new file called source.file with some data as shown below.

```bash 
$ echo "Hello Yogendra" >source.file
```

Now, create the a symbolic or soft link to the source.file

```bash
$ ln -s source.file softlink.file
```

Let us compare the data of both source.file and softlink.file

```bash
$ cat source.file 
Welcome to OSTechNix
```

```bash
$ cat softlink.file 
Welcome to OSTechNix
```

Let us check the inodes and permissions of softlink.file and source.file

```bash
$ ls -lia
```

