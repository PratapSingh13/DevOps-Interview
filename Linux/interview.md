- **User root has created a file(/tmp/abc) with 700 permission, you want that user named tom should have full access to file, how will do this ?**

    For this we can set ACLs for the tom user in required file

    ```setfacl -m u:tom:rwx /tmp/abc```

- **How will you change the default login shell for all upcoming users on Linux?**

    There are two main files by which we can modify for this is ```/etc/login.defs``` and ```/etc/default/useradd```

- **After creating password less ssh access, whenever I try to login to a server it asks me for the password, While I have verified that my public key is placed on a remote server?**

    For this we can follow few steps:


    - First we need to check the permission of the file it should have between 400 to 644.

    - ```ssh-add``` connection should be established properly.

- **How to disable root account?**

    ```sudo usermode -s /sbin/nologin root```
    
    To enable it again we can use

    ```sudo usermod -s /bin/bash root``` 

- **I have a server where httpd service is running, I want that httpd should be running on,cpu core 2 only.(CPUAffinity=2)**

    So here it want to bind httpd to specific CPU. To achieve this we need to change CPU Affinity value in httpd service file which can be found on either ```/usr/lib/systemd/system/httpd.service``` or ```/etc/systemd/system/httpd.service```

- **I want to restart a service only if the service is already running If service is in a stopped state, the command should do nothing.**

    ```systemctl try-restart httpd.service```

- **What is max filename length allowed in Linux?**

    255 characters

- **How would you conduct RCA for sudden surge of RAM on a linux server and ensure it doesn't repeat?**

    If I talk about how I will conduct RCA for sudden surge of RAM on a linux server so for this I will check the log entry that will be generated usually available in /var/log/ location. 
    using the command ```grep -i -r 'out of memory' /var/log/```

    To check the current memory usage in the server. we can use the command *“free”* to find the current memory usage in the server.
    using the command ```free -m```

    The history of memory usage for the day can be found by using the “sar” command.
    using the command ```sar -r```

    Another good tool to identify the Memory consuming processes is the “top” or "htop" command, 
    which will give us the option to sort the running processes based on its resource usages.

    using the command ```top -c```

    Tackle the memory overload
    We can find the server time at which this ‘out of memory’ was reported, suppose here it is “Jul 29 10:24:05”. 
    Use grep command to search this timestamp in the log files for your application servers like Apache, MySQL etc.

    using the command grep  -ir “29/Jul/2022:10:2”  /usr/local/apache/domlogs/

    A RAM upgrade is necessary if the server shows consistent high memory usage or the average usage for the day is more than 90% as such a high usage can deplete the available free memory at times for a busy server.

- *How can you identify listening ports on a Centos EC2 instance without AWS console or ssh access?*

    Bash has been able to access TCP and UDP ports for a while.
    So for this we can use
    ```bash
    cat < /dev/tcp/127.0.0.1/22
    SSH-2.0-OpenSSH_6.2p2 Debian-6
    ^C pressed here
    ```



