#!/usr/bin/env python
import random
import csv
from collections import defaultdict

from environs import Env
from simple_salesforce import Salesforce, format_soql

env = Env()
env.read_env()

salesforce = Salesforce(
    username=env("USERNAME"), password=env("PASSWORD"), security_token=env("TOKEN")
)


def create_accounts(count):
    data = [{"Name": f"Account - {x}"} for x in range(count)]
    return salesforce.bulk.Account.insert(data, batch_size=1000, use_serial=True)


def create_opportunities(account, count):
    data = [
        {
            "Name": f"Opportunity - {x}",
            "StageName": "new",
            "CloseDate": "2021-12-12",
            "AccountId": account["id"],
            "Amount": random.randint(10000, 100000),
        }
        for x in range(count)
    ]
    return salesforce.bulk.Opportunity.insert(data, batch_size=1000, use_serial=True)


def create_report(accounts):
    ids = [x["id"] for x in accounts]
    query = format_soql(
        "select Id, Name from Account where id in {ids}",
        ids=ids,
    )
    account_data = salesforce.bulk.Account.query(query, lazy_operation=True)

    accounts_revenue = defaultdict(lambda: {"Name": "", "Revenue": 0})
    for batch in account_data:
        for account in batch:
            accounts_revenue[account["Id"]]["Name"] = account["Name"]

    query = format_soql(
        "select AccountId, Amount from Opportunity where AccountId in {ids}",
        ids=ids,
    )
    fetch_results = salesforce.bulk.Opportunity.query(query, lazy_operation=True)

    for batch in fetch_results:
        for record in batch:
            accounts_revenue[record["AccountId"]]["Revenue"] += record["Amount"]

    return accounts_revenue


def create_csv(report_data):
    with open('result.csv', 'w') as writer:
        csv_writer = csv.writer(writer, delimiter=',')
        csv_writer.writerow(['ID', 'Name', 'Revenue'])
        for key in report_data:
            csv_writer.writerow([key, report_data[key]['Name'], report_data[key]['Revenue']])


def main():
    accounts = create_accounts(5)
    for account in accounts:
        create_opportunities(account, 2)

    report_data = create_report(accounts)
    create_csv(report_data)


if __name__ == "__main__":
    main()
