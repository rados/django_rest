# Simple Django Rest Framework Example

## Intsallation

There is a requirements.txt file.

## Use

There is admin panel for the models that could be used to create content. Also the REST API accepts requests, you can use curl or Postman.

Orders are created on two steps. First we create and empty order (with empty products list). Then we use PATCH request to pass the products list to the newly created order.

There is basic swagger documentation here: swagger/schema/

We can get stats by providing date range and a metric, for example:
http://127.0.0.1:8000/api/stats?date_start=2022-01-01&date_end=2022-09-01&metric=price