
# Test assignment for Backend developer
#### Python 3.11, Django 4.2, DRF, PostgreSQL, Docker

### Developed according the task:

#### "Your task is creating a simple product inventory management system. The system should allow users to add, update, delete, and list establishments and products in the inventory"
1. API Development. Crud, listing for establishment and product. Pagination for listings.
2. Docker Compose. Dockerized with postgresql. Dockerfile and docker-compose can be found
3. Swagger Documentation. localhost:8000/api/schema/swagger-ui/
4. Suite ofUnit Tests. Used unittest for endpoints testing. 'python3 manage.py test' to execute tests
5. PostgreSQL Integration. Integrated locally and in docker container


#### Swagger localhost/api/schema/swagger-ui/

## Preparation for launch:
1. You need to fill out the file ".env.dev". Example - ".env.dev-example". 

## Launch:
    1.  docker-compose build
    2.  docker-compose up
    * Tests will run shortly after "up" command. Result would be seen in terminal
    * Tests can be launched by using command "docker-compose run test"
    * Tests can be launched in docker by using command "python3 manage.py test"

## API Guide:


### Listing of Establishment or Product:

#### Request

`GET /api/v1/product/list/` 
or
`GET /api/v1/establishment/list/`

#### With pagination param

`GET /api/v1/product/list/?page=1` 
or
`GET /api/v1/establishment/list/?page=1`

#### Response
    
    {"count":10,"next":"http://localhost:8000/api/v1/product/list/?page=2","previous":null,"results":[{"id":1,"name":"one1","description":"1321","price":"222.40","quantity":11},{"id":2,"name":"two2","description":"dsadkl","price":"2131.00","quantity":1},{"id":3,"name":"three","description":"3","price":"333.00","quantity":3},{"id":4,"name":"new_productk4","description":"new_textr","price":"8882.00","quantity":42},{"id":5,"name":"five","description":"55","price":"555.50","quantity":5}]}


### Creating of Establishment or product

#### Request

`POST /api/v1/product/create/` 
    
    {
        "name": "string",
        "description": "string",
        "price": "17138600",
        "quantity": 2147483647
    }

or

`POST /api/v1/establishment/create/`

    {
      "name": "string",
      "description": "string",
      "locations": "string",
      "opening_hours": "7-24"
    }
* When creating establishment "opening_hours" must be in format "7-24", "12-23" 

#### Response

    {
        "id": 1,
        "name": "string",
        "description": "string",
        "price": "17138600",
        "quantity": 2147483647
    }

or

    {
        "id": 1,
        "name": "string",
        "description": "string",
        "locations": "string",
        "opening_hours": "7-24"
    }


### Get a specific Establishment or Product

#### Request

`GET /api/v1/product/1/` 
or
`GET /api/v1/establishment/1/`

#### Response
    {
      "id": 1,
      "name": "one1",
      "description": "1321",
      "price": "222.40",
      "quantity": 11
    }

or

    {
      "id": 1,
      "name": "estab1",
      "description": "descr",
      "locations": "layofette",
      "opening_hours": "7-24"
    }

### Change existing Establishment or Product

#### Request
    
`PUT /api/v1/product/1/` 

    {
      "name": "string",
      "description": "string",
      "price": "935073.58",
      "quantity": 0
    }

or

`PUT /api/v1/establishment/1/` 

    {
      "name": "string",
      "description": "string",
      "locations": "string",
      "opening_hours": "7-24"
    }
* When updating establishment "opening_hours" must be like  "7-24", "12-23" 

#### Response

    {
      "id": 1,
      "name": "string",
      "description": "string",
      "price": "935073.58",
      "quantity": 0
    }

or

    {
      "id": 1,
      "name": "string",
      "description": "string",
      "locations": "string",
      "opening_hours": "7-24"
    }


### Partially change existing Establishment or Product

#### Request
    
`PATCH /api/v1/product/1/` 

    {
      "price": "935073.58",
      "quantity": 0
    }

or

`PATCH /api/v1/establishment/1/` 

    {
      "locations": "string",
      "opening_hours": "7-24"
    }
* When creating establishment "opening_hours" must be like "7-24", "12-23"

#### Response

    {
      "id": 1,
      "name": "string",
      "description": "string",
      "price": "935073.58",
      "quantity": 0
    }

or

    {
      "id": 1,
      "name": "string",
      "description": "string",
      "locations": "string",
      "opening_hours": "7-24"
    }


### Delete existing Establishment or Product

#### Request

`DELETE /api/v1/or/1/`
or
`DELETE /api/v1/establishment/1/`

#### Response
    204 no response body
