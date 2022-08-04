## How to handle a Linux kernel panic
-   **What is a kernel panic?**

    Kernel panic is "a system error that cannot be recovered from, and requires the system to be restarted." As we all know, a forced restart is never good.

    As a result of the system needing to be rebooted, valuable debugging information like what is in the system’s memory at the time of the panic, will be lost when the system comes back up.
    To collect that information, which might be very valuable for troubleshooting purposes, it is important to configure a core collection method ahead of time.
    kdump helps to provides a crash dumping mechanism. The service enables you to save the contents of the system memory for analysis.