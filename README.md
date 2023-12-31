# AdProfit_test_task

Implementation of revenue and spend endpoints with specified models.

## Installation

Python 3 should be installed.

    https://github.com/Oomamchur/AdProfit_test_task
    cd AdProfit_test_task
    python -m venv venv

On Windows:
    
    source venv\Scripts\activate

On macOS or Linux:

    source venv/bin/activate

This project uses environment variables to store sensitive information such as the Django secret key and database credentials.
Create a `.env` file in the root directory of your project and add your environment variables to it. This file should not be committed to the repository.
You can see the example in `.env.sample` file.

    pip install -r requirements.txt
    python manage.py migrate    
    python manage.py runserver

## Getting access
Use the following command to load prepared data from fixture to test and see results:

    python manage.py loaddata fixture_data.json


    access to spend endpoint: /api/spend/
    access to revenue endpoint: /api/revenue/
