#!/usr/bin/env python
from environs import Env
from simple_salesforce import Salesforce

env = Env()
env.read_env()

salesforce = Salesforce(
    username=env("USERNAME"), password=env("PASSWORD"), security_token=env("TOKEN")
)
print(dir(salesforce.Contact))
