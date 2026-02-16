# How to create secrets in secret manager and use in AWS EKS

Below is the correct, production-ready workflow to:
- Create a secret in AWS Secrets Manager
- Mount it inside pods running on Amazon EKS
- Using IRSA + Secrets Store CSI Driver (recommended approach)

### High level overview

```code
Pod
  ↓
Secrets Store CSI Driver
  ↓
AWS Provider Plugin
  ↓
IAM Role (IRSA via OIDC)
  ↓
AWS Secrets Manager
```

## ✅ STEP 1 — Create Secret in AWS Secrets Manager

```bash
aws secretsmanager create-secret \
  --name prod/app/db-credentials \
  --region ap-south-1 \
  --secret-string '{
    "username":"admin",
    "password":"SuperSecure123"
  }'
```

verify secret

```bash
aws secretsmanager get-secret-value \
  --secret-id prod/app/db-credentials \
  --region ap-south-1
```

## ✅ STEP 2 — Ensure OIDC Is Associated (IRSA Required)

Now verify IAM OIDC provider exists:

```bash
aws iam list-open-id-connect-providers
```

if missing 

```bash
eksctl utils associate-iam-oidc-provider \
  --region ap-south-1 \
  --cluster <cluster_name> \
  --approve
```

## ✅ STEP 3 — Install Secrets Store CSI Driver

Install via Helm (recommended)

```bash
helm repo add secrets-store-csi-driver \
  https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts

helm install csi-secrets-store \
  secrets-store-csi-driver/secrets-store-csi-driver \
  --namespace kube-system
```

## ✅ STEP 4 — Install AWS Provider Plugin

```bash
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml
```

Verify:

```bash
kubectl get pods -n kube-system | grep secrets
```

## ✅ STEP 5 — Create IAM Policy For Secret Access

Create `policy.json`:

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
      "Resource": "arn:aws:secretsmanager:ap-south-1:590379872770:secret:prod/app/db-credentials-*"
    }
  ]
}
```

Create policy

```bash
aws iam create-policy \
  --policy-name EKSSecretsAccessPolicy \
  --policy-document file://policy.json
```

## ✅ STEP 6 — Create IAM Role + Service Account (IRSA)

```bash
eksctl create iamserviceaccount \
  --name secrets-sa \
  --namespace default \
  --cluster learning \
  --attach-policy-arn arn:aws:iam::590379872770:policy/EKSSecretsAccessPolicy \
  --approve
```
**This does:**
- Creates IAM role
- Creates Kubernetes ServiceAccount
- Links them via OIDC trust

Verify:

```bash
kubectl get sa secrets-sa -o yaml
```

You should see annotation:

```yaml
eks.amazonaws.com/role-arn
```

## ✅ STEP 7 — Create SecretProviderClass

Create `secretproviderclass.yaml`:

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-db-secrets
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "prod/app/db-credentials"
        objectType: "secretsmanager"
        jmesPath:
          - path: username
            objectAlias: db-username
          - path: password
            objectAlias: db-password
```

Apply:

```bash
kubectl apply -f secretproviderclass.yaml
```


## ✅ STEP 8 — Mount Secret in Pod

Create `pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-app
spec:
  serviceAccountName: secrets-sa
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - name: secrets-store
          mountPath: "/mnt/secrets"
          readOnly: true
  volumes:
    - name: secrets-store
      csi:
        driver: secrets-store.csi.k8s.io
        readOnly: true
        volumeAttributes:
          secretProviderClass: aws-db-secrets
```

Apply:

```bash
kubectl apply -f deployment.yaml
```

## ✅ STEP 9 — Verify Inside Pod

```bash
kubectl exec -it test-app -- ls /mnt/secrets
```

**You should see:**

```
db-password
db-username
```

## ✅ STEP 10 — Verify Rotation (Optional)

Update secret in AWS:

```bash
aws secretsmanager update-secret \
  --secret-id prod/app/db-credentials \
  --region ap-south-1 \
  --secret-string '{"username":"admin","password":"NewSecurePassword123"}'
```

Wait for sync (default 60s):

```bash
kubectl exec -it my-app -- cat /mnt/secrets/db-password
```

## ✅ STEP 11 — Cleanup (Optional)

```bash
kubectl delete pod my-app
kubectl delete secretproviderclass aws-db-secrets
kubectl delete sa secrets-sa
aws iam delete-policy --policy-arn arn:aws:iam::590379872770:policy/EKSSecretsAccessPolicy
```

## 💡 Important Notes

### 1. Secret rotation
- Pods automatically sync secrets when they rotate (default 60 seconds)
- No pod restart needed

### 2. Multiple secrets
- Add more objects to `SecretProviderClass`
- All synced automatically

### 3. Error handling
- Pods won't start if secrets can't be fetched
- Check logs: `kubectl logs my-app`

## 🎯 Why This Approach?

✅ No secrets in Git \
✅ No base64 encoding \
✅ Automatic rotation \
✅ IAM-based authentication (no API keys) \
✅ Production-ready \

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
