# AWS SigV4 Calculator

This project provides a Python script to calculate AWS Signature Version 4 (SigV4) for AWS API requests. It demonstrates how to sign requests to AWS services using the SigV4 process.

[日本語のREADMEはこちら](README_ja.md)

## Features

- Calculates AWS SigV4 signature
- Sends a sample request to AWS IAM ListUsers API
- Provides debug information about the signing process

## Requirements

- Python 3.7+
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/aws-sigv4-calculator.git
   cd aws-sigv4-calculator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Update the `aws_sigv4_calculator.py` file with your AWS credentials:
   ```python
   access_key = 'YOUR_ACCESS_KEY'
   secret_key = 'YOUR_SECRET_KEY'
   ```

## Important Security Note

WARNING: It is not recommended to set AWS credentials directly in the code as shown in the example.
For production environments, please use environment variables or AWS credential providers to securely manage your credentials.

## Usage

Run the script:

```
python aws_sigv4_calculator.py
```

The script will output the response code, response body, and debug information including the Canonical Request, String to Sign, and Authorization Header.

## Response Sample

```xml
Response code: 200
Response body: 
<ListUsersResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListUsersResult>
    <IsTruncated>false</IsTruncated>
    <Users>
      <member>
        <Path>/</Path>
        <UserName>Admin</UserName>
        <UserId>AIDAEXAMPLEUSERID</UserId>
        <Arn>arn:aws:iam::123456789012:user/Admin</Arn>
        <CreateDate>2023-01-01T00:00:00Z</CreateDate>
      </member>
    </Users>
  </ListUsersResult>
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</ListUsersResponse>
```

## Purpose of this Repository

The main purpose of this repository is to demonstrate how to manually calculate the SigV4 signature required for AWS API requests when the AWS SDK or CLI cannot be used. This is useful in situations such as:

- Special environments requiring custom implementation
- Development in languages or platforms not supported by AWS SDKs
- When a detailed understanding of AWS authentication process is needed

This code implements the signature calculation flow described in the [official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/create-signed-request.html). Users can refer to this code to understand the SigV4 signing process or reuse it in their own projects as needed.

## Security Note

Never commit your AWS credentials to version control. The provided script uses hardcoded credentials for demonstration purposes only. In a production environment, use environment variables or AWS credential providers to securely manage your credentials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.