# api-labs

A collection of progressively challenging labs to help learning the fundamentals of API development. The APIs are described in OAS 3.0.0 using YAML and were implemented in Python 3.8.9 with the following modules/packages:  

* sqlite3: an embedded SQL database (part of Python's standard library) 
* fastapi==0.75.2: a web framework for building APIs 
* fastapi-code-generator==0.3.4: an OAS API code generator for fastapi 
* uvicorn==0.17.6: a lightweight web server  
* SQLAlchemy==1.4.35: an object-relational mapper 
* sqlacodegen==2.3.0: a database introspection tool that generates SQLAlchemy models automatically 
* yamlgen: an in-house database introspection tool that generates data schema types in YAML and based on OAS

Each lab is described in detailed steps to facilitate its use by students with no previous experience. 

I hope you enjoy these labs. Suggestions and contributions are welcomed. Thanks!

## Index

[Lab-00 - Quotes API (baseline)](lab-00)

The goal of this lab is to implement an API that returns a random quote. No database is required for this API and the quotes are hard-code favoring simplicity. 

[Lab-02 - Quotes API  + SQL Database](lab-02)

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 01](lab-01). However, this time the quotes are stored in an embedded SQL database (sqlite). Also, object-relational mapping was implemented using SQLAlchemy.

[Lab-03 - Quotes API  + SQL Database + Query Parameter](lab-03)

The goal of this lab is to implement an API that returns a random quote, with the same requirements of [Lab 02](lab-02). However, this implementation allows users to request that the returned random quote has a specific tag. 
