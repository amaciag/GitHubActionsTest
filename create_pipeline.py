from google.cloud import secretmanager
import kfp
from kfp import dsl
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


@dsl.pipeline(
    name='test-hello'
)
def test_hello(image='gcr.io/dbce-dswb-sbx-e07f/test_image:1.0.0',
               name='there'):
    hello = dsl.ContainerOp(name='hello',
                            image=image,
                            command=['python', 'greeting.py'],
                            arguments=['--name', name])


kfp.compiler.Compiler().compile(test_hello, './test_hello.yaml')
kfp_client.create_run_from_pipeline_package('./test_hello.yaml', arguments={}, namespace='maciag-am')
print('Pipeline Created!')