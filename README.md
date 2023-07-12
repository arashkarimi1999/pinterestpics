# PinterestPics 


PinterestPics is a pinterest scraper that reads from a sqlite of jobs created by rest api and stores links in mongodb so can be delivered with graphql.

## Installation

Pull and use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r /requirements/requirements.txt
```
Use alembic to create sqlite database and migrations.
```bash
alembic revision --autogenerate -m "create job model"
alembic upgrade head
```
Create a mongodb database on `localhost:27017`.\
Add a `chromedriver` to root of project.

## Usage
Run `jobs/main.py` and add your jobs to `localhost:8000/jobs/`.\
Example:
```json
{
    "item": "laptop",
    "count": 30
}
```
Run `pinterest_web_driver.py`.\
Run `items/main.py` and get your image links by graphql query to `localhost:8000/graphql`.\
Example:
```graphql
query{
    treeItems: item(filter:"tree", first:10){
        link
    }
    carItems: item(filter:"car", first:5){
        link
        tag
    }
}
```
