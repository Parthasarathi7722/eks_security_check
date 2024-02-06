# AWS EKS Security Checklist Script

## Overview

This Python script checks an AWS EKS (Elastic Kubernetes Service) cluster against a security checklist and generates a CSV report. The checklist includes various security measures recommended for EKS clusters.

## Prerequisites

- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- AWS credentials with necessary permissions

## Usage

1. Clone or download the repository to your local machine.

```bash
git clone https://github.com/your-username/eks-security-check.git
```

2. Navigate to the project directory.

```bash
cd eks-security-check
```

3. Run the script using Python 3.

```bash
python3 eks_security_check.py
```

4. Enter the requested AWS credentials and EKS cluster name as prompted.

5. The script will perform security checks and generate a CSV report (`eks_security_report.csv`).

## Checklist Items

- [ ] Application processes do not run as root.
- [ ] Privilege escalation is not allowed.
- [ ] The root filesystem is read-only.
- [ ] The default (masked) /proc filesystem mount is used.
- [ ] The host network or process space should NOT be used.
- [ ] Unused and unnecessary Linux capabilities are eliminated.
- [ ] Use SELinux options for more fine-grained process controls.
- [ ] Give each application its own Kubernetes Service Account.
- [ ] If a container does not need to access the Kubernetes API, do not let it mount the service account credentials.

## Notes

- This script uses the Boto3 library for AWS API interactions.
- Ensure that your AWS credentials have the necessary permissions to describe the EKS cluster.

---
