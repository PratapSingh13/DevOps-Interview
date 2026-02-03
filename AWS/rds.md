## RDS read replicas

* Create Read Replicas to scale the Read queries, thereby relieving pressure on the **Primary DB**.
* Data is only written to the Primary DB and can be read from any read replicas.
* Create up to 15 Read Replicas in the **same or different AWS region**.
* Data is replicated asynchronously.
* Promote the read replica to a standalone DB in case of failure of the Primary DB instance.

** Use cases**
1. Business reporting and data warehousing, where queries can run against a read replica, instead of the production DB instance.
2. Implementing disaster recovery.
3. Read data with low latency from the local region(where the end user can be) even if the Primary DB is in another region.

## RDS Multi-AZ deployment

* Primary DB instance in one AZ and standby DB instance(s) in another AZ.
* Application reads from and writes to only Primary DB.
* Data is synchronously replicated from Primary DB to Standby DB.
* In case of Primary DB failure or AZ failure, Standby DB is made Primary, and the DB endpoint points to Standby.
* Applications automatically get redirected to standby for read/write queries.

## Amazon RDS - important to know

* RDS supports automatic continuous backups and on-demand or scheduled snapshots.
* With continuous backups, we can do point-in-time restore (specific time with 1 sec granularity up to a maximum of 35 days)
* RDS snapshots are stored in S3. We can share the snapshot across AWS accounts or copy it across AWS regions to create a new database.
* Provide monitoring dashboards to monitor database performance metrics such as Database connections, CPU Utilisation, Free storage space, disk I/O etc.
* There is a 30 mins maintenance window for upgrades, which can be chosen by the customer.

### *Remember - You do not get access to underlying EC2 instances which host RDS*
