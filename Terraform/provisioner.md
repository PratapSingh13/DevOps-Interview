## What is Provisioner
Provisioners are used for executing scripts or shell commands on a local or remote machine as part of resource creation/deletion. They are similar to “EC2 instance user data” scripts that only run once on the creation. Terraform doesn’t run these scripts multiple times. If we want more flexibility then we must use a configuration management tool like ansible to properly provision the instance.

**File Provisioner** used to copy files or directories to the newly created resources and underneath it’s using ssh or winrm. Does the job of an scp.

```
resource "null_resource" "configure-vm" {

  connection {
      type = "ssh"
      user = var.username
      host = var.ip_address
      private_key = var.tls_private_key
    }

    ## Copy files to VM :
    provisioner "file" {
        source = "/Users/zakariaelbazi/Documents/GitHub/zackk8s/kubernetes"
        destination = "/home/${var.username}"
    }
}
```

**local-exec** provisioner helps run a script on instance where we are running our terraform code, not on the resource we are creating. For example, if we want to write EC2 instance IP address to a file, then we can use below local-exec provisioner with our EC2 resource and save it locally in a file.

```
resource "aws_instance" "testInstance" {
  ami                    = "${var.instance_ami}"
  instance_type          = "${var.instance_type}"
  subnet_id              = "${aws_subnet.subnet_public.id}"
  vpc_security_group_ids = ["${aws_security_group.sg_22.id}"]
  key_name               = "${aws_key_pair.ec2key.key_name}"
tags {
        "Environment"    = "${var.environment_tag}"
  }
  provisioner "local-exec" {
    command              = "echo ${aws_instance.testInstance.public_ip} >> public_ip.txt"
  }
}
```

**remote-exec** provisioner helps invoke a script on the remote resource once it is created. We can provide a list of command strings which are executed in the order they are provided. We can also provide scripts with a local path which is copied remotely and then executed on the remote resource. file provisioner is used to copy files or directories to a remote resource. We can’t provide any arguments to script in remote-exec provisioner. We can achieve this by copying script from file provisioner and then execute a script using a list of commands.

Provisioner which execute commands on a resource (like running a script or copying file)needs to connect to the resource which can be done through SSH. We can define connection method per resource or per provisioner if we want them to connect using different SSH parameters.

```
resource "aws_instance" "testInstance" {
  ami           = "${var.instance_ami}"
  instance_type = "${var.instance_type}"
  subnet_id = "${aws_subnet.subnet_public.id}"
  vpc_security_group_ids = ["${aws_security_group.sg_22_80.id}"]
  key_name = "${aws_key_pair.ec2key.key_name}"
  tags {
        "Environment" = "${var.environment_tag}"
    }
  provisioner "remote-exec" {
    inline = [
      "sudo amazon-linux-extras enable nginx1.12",
      "sudo yum -y install nginx",
      "sudo systemctl start nginx",
    ]
  }
  connection {
    type     = "ssh"
    user     = "ec2-user"
    password = ""
    private_key = "${file("~/.ssh/id_rsa")}"
  }
}
```

**Why you should avoid provisioner or use them only as a last resort ?**

First, Terraform cannot model the actions of provisioners as part of a plan, as they can in principle take any action (the possible commands is “limitless”) which means you won’t get anything about the provisioners in your tfstate. Even if you have them in null resources like I did.

Second, as you I mentioned above file and remote-exec provisioners require connection credentials to function and that adds unnecessary complexity to the Terraform configuration (Mixing day 1 and day 2 tasks).

So as HashiCorp recommends in the docs try using other techniques first, and use provisioners only if there is no other option but you should know them especially if you are planning to pass the Terraform certification exam.

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png