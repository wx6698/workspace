import requests

x = requests.get('cust-e2-us-west-2.cloud.databricks.com')
print(x.status_code)
print("heheß")