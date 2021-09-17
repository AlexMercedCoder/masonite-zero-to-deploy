"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "DogController@index").name("index"),
        Get("/@id", "DogController@show").name("show"),
        Post("/", "DogController@create").name("create"),
        Put("/@id", "DogController@update").name("update"),
        Delete("/@id", "DogController@destroy").name("destroy"),
    ], prefix="/dogs", name="dogs")
]
