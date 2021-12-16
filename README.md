# Test Task

- Sign up for a salesforce developer org.
- Use python (py version 3.8 or later) simple-salesforce connector to do the following. (https://pypi.org/project/simple-salesforce/)
- Use the rest api to create a random number of Account objects between 10 - 100.
- Use the rest api to create a random number of Opportunities between 0 - 5 for each Account in the previous step. These Opportunities should get a Revenue value randomly selected between $10,000 and $100,000
- Use the rest api to query for and provide a sum total of Revenue values per Account created in step 3. Create a CSV with the Id, Name and Total Revenue to contain these results.
- Document and unit test code as appropriate

Should take 3-6 hours

You can send us a repo link or zip file with the code when completed and we will review ASAP

## Installation

Create virtual environment.

    python3 -m venv venv

Activate virtual environment. You need to activate virtual environment before running any Django command. For example, any command starting with manage.py is a Django command.

    source venv/bin/activate

Install dependencies in virtual environment. You will have to run this command whenever you pull new changes from the server.

    pip install -r requirements.txt

Create an environment file (.env) in the root of the project. You can get the initial file by copying env.sample to .env. The .env file expects the following keys.

- USERNAME: Your Salesforce username.
- PASSWORD: Your Salesforce password.
- TOKEN: The security token associated with your Salesforce account.

## Execution

To run code:

    python main.py

You will get the result in `report.csv`.

## Test

To run tests:

    python tests.py

## Setup pre-commit

This project uses [pre-commit](https://pre-commit.com/) to ensure that code standard checks pass locally before pushing to the remote project repo. [Follow](https://pre-commit.com/#installation) the installation instructions, then set up hooks with `pre-commit install`.

Make sure everything is working correctly by running

    pre-commit run --all
