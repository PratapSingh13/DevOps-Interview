- **User root has created afile(/tmp/abc) with 700 permission, you want that user named tom should have full access to file, how will do this ?**

    For this we can set ACLs for the tom user in required file

    ```setfacl -m u:tom:rwx /tmp/abc```

- **How will you change the default login shell for all upcoming users on Linux?**

    There are two main files named which we can modifie for this is ```/etc/login.defs``` and ```/etc/default/useradd```

- **After creating password less ssh access, whenever I try to login to a server it asks me for the password, While I have verified that my public key is placed onaremote server?**

    For this we can follow few steps:


    - First we need to check the permission of the file it should have between 400 to 644.

    - ```ssh-add``` connection should be established properly.

- **How to disable root account?**

    ```sudo usermode -s /sbin/nologin root```
    
    To enable it again we can use

    ```sudo usermod -s /bin/bash root``` 

- **I have a server where httpd service is running, I want that httpd should be running on,cpu core no 2only.(CPUAffinity=2)**

    So here it want to bind httpd to specific CPU. To achieve this we need to change CPUAffinity value in httpd service file which can be found on either ```/usr/lib/systemd/system/httpd.service``` or ```/etc/systemd/system/httpd.service```

- **I want to restart a service only if the service is already running If service is in a stopped state, the command should do nothing.**

    ```systemctl try-restart httpd.service```

- **What is max filename length allowed in Linux?**

    255 characters




