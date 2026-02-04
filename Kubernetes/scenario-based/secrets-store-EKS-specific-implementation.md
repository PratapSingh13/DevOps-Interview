## Native EKS + AWS Secrets Manager

In EKS, I store DB credentials in AWS Secrets Manager and inject them into pods using IRSA and the Secrets Store CSI Driver, ensuring encryption, automatic rotation, zero hardcoded secrets, and least-privilege IAM access.

#### Step 1️⃣ Store DB Credentials in AWS Secrets Manager

```json
{
  "username": "db_user",
  "password": "StrongPassword123!",
  "host": "db.endpoint.amazonaws.com",
  "port": "5432"
}
```

✔ Encrypted at rest (KMS)
✔ Versioning + rotation supported

#### Step 2️⃣ Enable IRSA (IAM Role for Service Account)

**Create IAM policy:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:ap-south-1:123456789012:secret:db-secret-*"
    }
  ]
}
```

Attach this policy to an **IAM Role.**

#### Step 3️⃣ Create Kubernetes ServiceAccount (IRSA)

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: app-ns
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/eks-db-secret-role
```

✔ Pod now assumes IAM role securely
✔ No static AWS keys anywhere

#### Step 4️⃣ Install Secrets Store CSI Driver (EKS)

```bash
helm repo add secrets-store-csi-driver \
  https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts

helm install csi-secrets-store \
  secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system
```

**Install AWS provider:**

```bash
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml
```

#### Step 5️⃣ Create SecretProviderClass

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-db-secret
  namespace: app-ns
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "db-secret"
        objectType: "secretsmanager"
        jmesPath:
          - path: username
            objectAlias: DB_USER
          - path: password
            objectAlias: DB_PASSWORD
```

#### Step 6️⃣ Mount Secret into Pod

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      serviceAccountName: app-sa
      volumes:
      - name: secrets-store
        csi:
          driver: secrets-store.csi.k8s.io
          readOnly: true
          volumeAttributes:
            secretProviderClass: aws-db-secret
      containers:
      - name: app
        image: myapp:1.0
        volumeMounts:
        - name: secrets-store
          mountPath: "/mnt/secrets"
          readOnly: true
```

**Application reads:**

```bash
/mnt/secrets/DB_USER
/mnt/secrets/DB_PASSWORD
```

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
