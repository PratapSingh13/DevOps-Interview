# Introduction to kdump

kdump to be able to capture a kernel crash dump and save it for further analysis.

kdump is a service which provides a crash dumping mechanism. The service enables you to save the contents of the system memory for analysis.
kdump uses the kexec system call to boot into the second kernel (a capture kernel) without rebooting; and then captures the contents of the crashed kernel’s memory (a crash dump or a vmcore) and saves it into a file. 
The second kernel resides in a reserved part of the system memory.

### **Installing and configuring kdump**

The kdump service is installed and activated by default on the new Red Hat Enterprise Linux installations. 
We can enable kdump for all installed kernels on a machine or only for specified kernels. This is useful when there are multiple kernels used on a machine, 
some of which are stable enough that there is no concern that they could crash.

When kdump is installed, a default /etc/kdump.conf file is created. 
The file includes the default minimum kdump configuration. we can edit this file to customize the kdump configuration, but usually it is not required.

In order for kdump to be able to capture a kernel crash dump and save it for further analysis, a part of the system memory has to be permanently reserved for the capture kernel. 
When reserved, this part of the system memory is not available to the main kernel.

The memory requirements vary based on certain system parameters. 
One of the major factors is the system’s hardware architecture (such as Intel 64 and AMD64, also known as x86_64).

```bash
uname -m
```

**Installing kdump on the command line**

**Prerequisites**
-   An active RHEL subscription
-   The kexec-tools package
-   Fulfilled requirements for kdump configurations and targets.
1.  Check whether kdump is installed on your system:
    ```bash
    $ rpm -q kexec-tools
    ```

    Output if package is installed

    ```kexec-tools-2.0.17-11.el8.x86_64```
    
    Output if package is not installed

    ```
    package kexec-tools is not installed
    ```

2.  Install kdump and other necessary packages by:
    ```bash
    $ yum install kexec-tools
    ```

**Estimating the kdump size**

When planning and building your kdump environment, it is important to know how much space the crash dump file requires.

The ```makedumpfile --mem-usage``` command estimates how much space the crash dump file requires. 
It generates a memory usage report. The report helps you determine the dump level and which pages are safe to be excluded.
