API & GUI hosted in AWS Elastic Beanstalk
=============

This is an API with two HTTP endpoints that retrieves data & a GUI allowing users to CRUD data to a PostgreSQL database hosted in AWS RDS. Both were created in an AWS EC2 Amazon Linux 2 instance and successfully deployed to AWS Elastic Beanstalk. Python3.8

GUI Reference
-------------

The following is a reference guide for the graphical user interface (GUI) of this project.

### Adding a Product

#### "POST /add_product HTTP/1.1" 302


To add a product to the database, follow these steps:

1.  Navigate to the "/" page.
2.  Fill out the form with the necessary information.
3.  Click the "Save" button to submit the form.

If the product was added successfully, a success message will be displayed.

### Updating a Product

#### "GET /edit/{theme.id} HTTP/1.1" 200 
#### "POST /update/{theme.id} HTTP/1.1" 302


To update a product in the database, follow these steps:

1.  Navigate to db element and click the "edit" button

If the product was updated successfully, a success message will be displayed. 


### Deleting a Product

#### "GET /delete/{theme.id} HTTP/1.1" 302

To delete a product from the database, follow these steps:

1.  Navigate to db element and click the "delete" button.

If the product was deleted successfully, a success message will be displayed. 

Please note that all changes made to the database through the GUI are permanent and cannot be undone.


### Demo Section #1: GUI

Here's a video of the GUI in action:

https://user-images.githubusercontent.com/88054514/235284249-9ff7f9f9-a7b5-46ef-9fc9-a6fc024ca544.mp4



API Reference
-------------

### Endpoints

#### "GET /allproducts HTTP/1.1" 200

Returns JSON data of all products.

Example:

jsonCopy code
`
[
  {
    "id": 1,
    "name": "Product1",
    "ThumbnailURL": "example.com/product1-thumbnail.png",
    "SourceURL": "example.com/product1-source.png",
    "Category": "Category1"
  },
  {
    "id": 2,
    "name": "Product2",
    "ThumbnailURL": "example.com/product1-thumbnail.png",
    "SourceURL": "example.com/product1-source.png",
    "Category": "Category2"
  }
]
`

#### "GET /product/count/start HTTP/1.1" 200

Paginates through the data with the amount "count" of elements it'd like returned at start which is 1-indexed and which element it will start at. Returns JSON, returns nothing if count or start are N/A.

Parameters:

-   `count` (necessary): the number of elements to return
-   `start` (necessary): the 1-indexed position to start from 

Example:

Request: `GET /product/2/1`

Response:

jsonCopy code

`
[
  {
    "id": 1,
    "name": "Product1",
    "ThumbnailURL": "example.com/product1-thumbnail.png",
    "SourceURL": "example.com/product1-source.png",
    "Category": "Category1"
  },
  {
    "id": 2,
    "name": "Product2",
    "ThumbnailURL": "example.com/product1-thumbnail.png",
    "SourceURL": "example.com/product1-source.png",
    "Category": "Category2"
  }
]
`

If the data is successfully created, the API will return a `200 OK` response with the ID of the new data in the response body. Example:


### Demo Section #2: API

Here's a video of the API in action:


https://user-images.githubusercontent.com/88054514/235284208-817de5ba-0743-43d0-bea1-3bef8a12a316.mp4
