# Films

Website with list of films.

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

* __API filtering parameters__
    * URL: ```/api/films/```
    * by director:

      ```?director=<director id>```
    * by year:
      
      Greater than:
      ```?year_of_release__gt=<year>```
  
      Least than:
      ```?year_of_release__lt=<year>```
    * by actors:

      ```?actors=<actor id>```
    * by page:

      ```?page=<page>```
 
      Example:
      ```
      https://films-lake.vercel.app/api/films/?year_of_release__gt=1950&year_of_release__lt=2008&director=1&actors=65&actors=28
      ```
