# Films

Website with list of films.

### Usage
* configure ```.env``` file
* create and configure vitrual environment:
  ```
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
* start application:
  ```
  python manage.py runserver
  ```

  To use the API, make HTTP requests to the provided endpoints using your preferred HTTP client, such as curl or Postman.

### Endpoints

* __Get films list__
    * URL: ```/api/films/```
    * Method: GET
* __Add film__
    * URL: ```/api/add_film/```
    * Method: POST
    * Required fields: name, year_of_release, director, actors.

      Example:
      ```
      {
        "name": "Goodfellas",
        "year_of_release": "1990",
        "director": "Martin Scorsese",
        "actors": "Robert De Niro, Ray Liotta, Joe Pesci"
      }
      ```
* __Retrieve, Update, or Delete film__
    * URL: ```/api/films/<film_id>/```
    * Methods: GET, PUT, PATCH, DELETE