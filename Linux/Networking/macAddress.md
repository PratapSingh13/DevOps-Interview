# What is MAC address
MAC address stands for ***Media Access Control*** MAC address have multiple name like on Monbile we will found as **Physical Address** on laptop and PCs we will found as **Hardware Address** in CISCO router and switches we will found as **BIA(Burnt-in-Address).**

**The MAC address is always for hardware/physical device. which means MAC address is a unique identifier that is assigned to a NIC (Network Interface Controller/ Card). It consists of a 48 bit or 64-bit address, which is associated with the network adapter. MAC address can be in hexadecimal format. The full form of MAC address is Media Access Control address.** 

Few points to remember

-   MAC address is always globally unique.

-   We can have multiple MAC address on a single    laptop because it completely depends on number of NICs.

-   MAC address is of total 48bits equivalent to 6bytes.

-   On 48bits, 24bits are for OUI and 24bits are for vendor specific.

-   OUI can be only alloted by IANA and OUI will be always globally unique.

## MAC Address Vs. IP Address
-   Both IP address and MAC address assist in defining a device uniquely on the internet.

-   The manufacturer of the NIC Card provides a user with the MAC address while the ISP (Internet Service Provider) comes up with the IP address.

|**Parameters**                   | **MAC Address** | **IP Address**    |
|:-------------------:|:---------------:|:-----------------:|
| **Full-Form** | Media Access Control Address | Internet Protocol Address |
| **Number of Bytes** | It is a hexadecimal address of six bytes | This address is either an eight-byte or a six-byte one |
| **Protocol Used for Retrieval** | You can retrieve a device attached to the MAC address using the ARP protocol | You can retrieve a device attached to the IP address using the RARP protocol |
| **Use** | The primary use of a MAC address is to ensure the physical address of a given device/ computer | The IP address, on the other hand, defines a computer’s logical address |