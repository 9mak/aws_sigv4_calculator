import sys
import datetime
import hashlib
import hmac
import requests
from urllib.parse import quote

# AWS認証情報
access_key = 'xxxx'
secret_key = 'xxxx'
region = 'us-east-1'
service = 'iam'

# リクエスト情報
method = 'GET'
host = 'iam.amazonaws.com'
endpoint = f'https://{host}'
request_parameters = 'Action=ListUsers&Version=2010-05-08'

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

def create_canonical_request(method, canonical_uri, canonical_querystring, canonical_headers, signed_headers, payload_hash):
    return f"{method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}"

def create_string_to_sign(algorithm, request_date, credential_scope, canonical_request_hash):
    return f"{algorithm}\n{request_date}\n{credential_scope}\n{canonical_request_hash}"

# リクエスト日時
t = datetime.datetime.now(datetime.UTC)
amzdate = t.strftime('%Y%m%dT%H%M%SZ')
datestamp = t.strftime('%Y%m%d')

# ステップ1: 正規リクエストの作成
canonical_uri = '/'
canonical_querystring = request_parameters
canonical_headers = f'host:{host}\nx-amz-date:{amzdate}\n'
signed_headers = 'host;x-amz-date'
payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()

canonical_request = create_canonical_request(method, canonical_uri, canonical_querystring, canonical_headers, signed_headers, payload_hash)

# ステップ2: 署名文字列の作成
algorithm = 'AWS4-HMAC-SHA256'
credential_scope = f'{datestamp}/{region}/{service}/aws4_request'
canonical_request_hash = hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
string_to_sign = create_string_to_sign(algorithm, amzdate, credential_scope, canonical_request_hash)

# ステップ3: 署名の計算
signing_key = getSignatureKey(secret_key, datestamp, region, service)
signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

# ステップ4: リクエストへの署名の追加
authorization_header = f'{algorithm} Credential={access_key}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'

headers = {
    'x-amz-date': amzdate,
    'Authorization': authorization_header
}

# リクエストの送信
request_url = f'{endpoint}?{request_parameters}'
r = requests.get(request_url, headers=headers)

print(f'Response code: {r.status_code}')
print(f'Response body: {r.text}')

# デバッグ情報の出力
print("\nデバッグ情報:")
print(f"Canonical Request:\n{canonical_request}")
print(f"\nString to Sign:\n{string_to_sign}")
print(f"\nAuthorization Header:\n{authorization_header}")
