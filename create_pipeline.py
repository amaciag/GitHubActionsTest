from google.cloud import secretmanager
import kfp
import json
import argparse

    
client = secretmanager.SecretManagerServiceClient()
name = client.secret_version_path('dbce-dswb-sbx-e07f', 'kfp-connect', 'latest')
response = client.access_secret_version(name=name)

payload = response.payload.data.decode("UTF-8")
kfp_client = kfp.Client(host=payload.split(',')[0],
                        ssl_ca_cert=payload.split(',')[1],
                        client_id=payload.split(',')[2],
                        other_client_id=payload.split(',')[3],
                        other_client_secret=payload.split(',')[4])


print('job is running')
print(kfp_client.list_pipelines())