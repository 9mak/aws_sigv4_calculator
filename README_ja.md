# AWS SigV4 計算機

このプロジェクトは、AWS API リクエストのための AWS Signature Version 4 (SigV4) を計算する Python スクリプトを提供します。SigV4 プロセスを使用して AWS サービスへのリクエストに署名する方法を示しています。

[English README is here](README.md)

## 特徴

- AWS SigV4 署名の計算
- AWS IAM ListUsers API へのサンプルリクエストの送信
- 署名プロセスに関するデバッグ情報の提供

## 要件

- Python 3.7+
- `requests` ライブラリ

## インストール

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/aws-sigv4-calculator.git
   cd aws-sigv4-calculator
   ```

2. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

3. `aws_sigv4_calculator.py` ファイルを AWS 認証情報で更新します：
   ```python
   access_key = 'YOUR_ACCESS_KEY'
   secret_key = 'YOUR_SECRET_KEY'
   ```

## 重要なセキュリティに関する注意

警告: 例示されているように、コード内に直接AWS認証情報を設定することは推奨されません。
本番環境では、環境変数やAWS認証情報プロバイダーを使用して、認証情報を安全に管理してください。

## 使用方法

スクリプトを実行します：

```
python aws_sigv4_calculator.py
```

スクリプトは、レスポンスコード、レスポンスボディ、および正規リクエスト、署名対象文字列、認証ヘッダーを含むデバッグ情報を出力します。

## レスポンスサンプル

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

## このリポジトリの目的

このリポジトリの主な目的は、AWS SDK や CLI を使用できない場合に、AWS API リクエストに必要な SigV4 署名を手動で計算する方法を示すことです。これは、以下のような状況で役立ちます：

- カスタム実装が必要な特殊な環境
- AWS SDK がサポートしていない言語やプラットフォームでの開発
- AWS の認証プロセスの詳細な理解が必要な場合

このコードは、[AWS の公式ドキュメント](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/create-signed-request.html)に記載されている署名計算フローを実装しています。ユーザーはこのコードを参照し、SigV4 署名プロセスを理解したり、必要に応じて自身のプロジェクトに再利用したりすることができます。

## セキュリティに関する注意

AWS 認証情報をバージョン管理システムにコミットしないでください。提供されたスクリプトはデモンストレーション目的でのみハードコードされた認証情報を使用しています。本番環境では、環境変数や AWS 認証情報プロバイダーを使用して認証情報を安全に管理してください。

## ライセンス

このプロジェクトは MIT ライセンスの下で提供されています - 詳細は [LICENSE](LICENSE) ファイルを参照してください。