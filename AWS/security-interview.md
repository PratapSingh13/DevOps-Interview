- **What is the difference between Security groups vs Network ACLs** ?

  | **NACL** | **Security Group** |
  |:--------:|:------------------:|
  | NACL can be understood as the firewall or protection for the subnet | Security group can be understood as a firewall to protect EC2 instances |
  | It is considered to be the second layer of defence, which helps protect AWS stack. It is an optional layer for VPC, which adds another security layer to the amazon service | It is considered to be the first defence layer that helps protect the Amazon Web Services infrastructure | 
  | Multiple subnets can be bound with a single NACL, but one subnet can be bound with a single NACL only, at a time | Security groups are associated with an instance of a service. It can be associated with one or more security groups which has been created by the use |
  | These are stateless, meaning any change applied to an incoming rule isn’t automatically applied to an outgoing rule | These are stateful, which means any changes which are applied to an incoming rule is automatically applied to a rule which is outgoing |
  | In case of NACL, the rules are applied in the order of their priority, wherein priority is indicated by the number the rule is assigned | In case of a security group, all the rules are applied to an instance |
  | This means every rule is evaluated based on the priority it has | This means all rules are evaluated before they allow a traffic |
