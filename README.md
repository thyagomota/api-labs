# api-labs

A collection of progressively challenging labs to help learning the fundamentals of API development. The APIs are described in OAS 3.0.0 using YAML and were implemented in Python 3.8.9 with the following modules/packages:  

* sqlite3: an embedded SQL database (part of Python's standard library) 
* fastapi==0.75.2: a web framework for building APIs 
* fastapi-code-generator==0.3.4: an OAS API code generator for fastapi 
* uvicorn==0.17.6: a lightweight web server  
* SQLAlchemy==1.4.35: an object-relational mapper 
* sqlacodegen==2.3.0: a database introspection tool that generates SQLAlchemy models automatically 
requests==2.27.1: an HTTP library
* yamlgen: an in-house database introspection tool that generates data schema types in YAML and based on OAS

Each lab is described in detailed steps to facilitate its use by students with no previous experience. 

I hope you enjoy these labs. Feel free to contribute to this project or to adapt it as it fits your needs. Thanks!

## Index

[Lab-00 - Quotes API (baseline)](lab-00)

The goal of this lab is to implement an API that returns a random quote. No database is required for this API and the quotes are hard-code favoring simplicity. 

[Lab-01 - Quotes API  + SQL Database](lab-01)

The goal of this lab is to implement an API that returns a random quote, similarly to [Lab 00](lab-00). However, this time the quotes are stored in an (embedded) SQL database (sqlite). Also, object-relational mapping was implemented using SQLAlchemy.

[Lab-02 - Quotes API  + SQL Database + Path Parameter](lab-02)

The goal of this lab is to implement an API that returns a single quote, with the same requirements of [Lab 01](lab-01). In the previous lab, the <em>path</em> for a random quote was always set to zero. In this new lab the user can request a specific quote based on the quote's id indicated in the path. Because the requested quote might not exist, a 404 (Not Found) response was added to the API's specification.

[Lab-03 - Quotes API  + SQL Database + Path Parameter + Query Parameters](lab-03)

This lab is built on top of [Lab 02](lab-02) with the addition of (optional) query parameters. 

[Lab-04 - Quotes API + SQL Database + Path Parameter + Query Parameter + Pagination](lab-04)

API pagination gives users the ability to select which group of objects of the same type to return. This lab implements a limit-offset pagination of quotes that fit a given search criteria. 

[Lab-05 - Quotes API + SQL Database + Path Parameter + Query Parameter + Pagination + Authentication](lab-05)

A key parameter is added to Quotes API to provide a simple authentication mechanism. 