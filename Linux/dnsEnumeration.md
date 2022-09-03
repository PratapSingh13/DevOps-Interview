# How to do DNS Enumeration

## $ host

```bash
$ host opstree.com
```
The output should be like 

```
opstree.com has address 3.33.152.147
opstree.com has address 15.197.142.173
opstree.com has IPv6 address 2402:3a80:1fff:3f::321:9893
opstree.com has IPv6 address 2402:3a80:1fff:3f::fc5:8ead
opstree.com mail is handled by 10 alt3.aspmx.l.google.com.
opstree.com mail is handled by 10 alt4.aspmx.l.google.com.
opstree.com mail is handled by 5 alt1.aspmx.l.google.com.
opstree.com mail is handled by 5 alt2.aspmx.l.google.com.
opstree.com mail is handled by 1 aspmx.l.google.com.
```

**Specify the information that you looks for**

```bash
$ host -t ns opstree.com
```

From this you can get the nameserver details

```
opstree.com name server ns69.domaincontrol.com.
opstree.com name server ns70.domaincontrol.com.
```

To get the information about the mail server:

```bash
$ host -t mx opstree.com
```

From this you can get the mail server details

```
opstree.com mail is handled by 10 alt4.aspmx.l.google.com.
opstree.com mail is handled by 5 alt1.aspmx.l.google.com.
opstree.com mail is handled by 5 alt2.aspmx.l.google.com.
opstree.com mail is handled by 1 aspmx.l.google.com.
opstree.com mail is handled by 10 alt3.aspmx.l.google.com.
```

We can also resolve the host using the IP address which we got from DNS 

```bash
$ host 3.33.152.147
```

```
147.152.33.3.in-addr.arpa domain name pointer a4ec4c6ea1c92e2e6.awsglobalaccelerator.com.
```

```bash
$ host 15.197.142.173
```

```
173.142.197.15.in-addr.arpa domain name pointer a4ec4c6ea1c92e2e6.awsglobalaccelerator.com.
```

## $ nslookup

```bash
$ nslookup opstree.com
```

The output should be like 

```
Server:		192.168.43.253
Address:	192.168.43.253#53

Non-authoritative answer:
Name:	opstree.com
Address: 15.197.142.173
Name:	opstree.com
Address: 3.33.152.147
```

Let's discuss the details what we get

```Server: 192.168.43.253```

This is the DNS server that we are using.

```Address: 192.168.43.253#53```

This is the address of DNS server which found on port 53


```
Non-authoritative answer:
Name:	opstree.com
Address: 15.197.142.173
Name:	opstree.com
Address: 3.33.152.147
```

This gives the name and address only.