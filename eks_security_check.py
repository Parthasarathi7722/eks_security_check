import csv
import boto3

def get_aws_credentials():
    aws_access_key_id = input("Enter your AWS Access Key ID: ")
    aws_secret_access_key = input("Enter your AWS Secret Access Key: ")
    aws_session_token = input("Enter your AWS Session Token (if applicable, press Enter to skip): ")

    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'aws_session_token': aws_session_token
    }

def check_eks_security(aws_access_key_id, aws_secret_access_key, aws_session_token, cluster_name):
    # Initialize EKS client
    eks_client = boto3.client('eks', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              aws_session_token=aws_session_token)

    try:
        # Get cluster details
        cluster_info = eks_client.describe_cluster(name=cluster_name)
        cluster_security_group_id = cluster_info['cluster']['resourcesVpcConfig']['clusterSecurityGroupId']

        # Replace placeholder values with actual checks for each security checklist item
        application_processes_not_root = False
        privilege_escalation_not_allowed = False
        root_filesystem_read_only = False
        masked_proc_filesystem_used = False
        host_network_not_used = False
        unused_capabilities_eliminated = False
        selinux_options_used = False
        each_application_has_own_service_account = False
        container_no_kubeapi_access = False

        # Create a CSV report
        with open('eks_security_report.csv', 'w', newline='') as csvfile:
            fieldnames = ['Checklist Item', 'Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Checklist Item': 'Application processes do not run as root.', 'Status': application_processes_not_root})
            writer.writerow({'Checklist Item': 'Privilege escalation is not allowed.', 'Status': privilege_escalation_not_allowed})
            writer.writerow({'Checklist Item': 'The root filesystem is read-only.', 'Status': root_filesystem_read_only})
            writer.writerow({'Checklist Item': 'The default (masked) /proc filesystem mount is used.', 'Status': masked_proc_filesystem_used})
            writer.writerow({'Checklist Item': 'The host network or process space should NOT be used.', 'Status': host_network_not_used})
            writer.writerow({'Checklist Item': 'Unused and unnecessary Linux capabilities are eliminated.', 'Status': unused_capabilities_eliminated})
            writer.writerow({'Checklist Item': 'Use SELinux options for more fine-grained process controls.', 'Status': selinux_options_used})
            writer.writerow({'Checklist Item': 'Give each application its own Kubernetes Service Account.', 'Status': each_application_has_own_service_account})
            writer.writerow({'Checklist Item': 'If a container does not need to access the Kubernetes API, do not let it mount the service account credentials.', 'Status': container_no_kubeapi_access})

        print("CSV report generated: eks_security_report.csv")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    aws_credentials = get_aws_credentials()

    # Prompt user for AWS EKS cluster name
    eks_cluster_name = input("Enter your AWS EKS cluster name: ")

    # Run the security checks and generate the CSV report
    check_eks_security(
        aws_credentials['aws_access_key_id'],
        aws_credentials['aws_secret_access_key'],
        aws_credentials['aws_session_token'],
        eks_cluster_name
    )
