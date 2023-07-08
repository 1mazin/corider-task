# Flask CRUD Application with MongoDB

This is a Flask application that allows you to perform CRUD operations (Create, Read, Update, Delete) on a User resource using a REST API. The application utilizes the Flask framework and the PyMongo library to connect to a MongoDB database.

## Steps to setup 

1. Clone this repository to your local machine:

2. Navigate to the project directory:

3. Create a virtual environment for the project:
    ```
    python -m venv venv
    ```
   Activate the virtual environment:

        For Windows:
    ```
        venv\Scripts\activate
    ```
        For macOS/Linux:
    ```
        source venv/bin/activate
    ```
    

4. Install all the required dependencies by using the command given below:

   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to configure the MongoDB connection settings. Open the `config.py` file and update the connectionString with you mongodb connection string.



## To start the Flask application, run the following command:

```
python app.py
```


## API Endpoints

The following REST API endpoints are available:

- `GET /users`: Returns a list of all users.
- `GET /users/<id>`: Returns the user with the specified ID.
- `POST /users`: Creates a new user.
- `PUT /users/<id>`: Updates the user data with specified ID.
- `DELETE /users/<id>`: Deletes the user with the specified ID.

Use a tool like Postman to test the API endpoints by sending HTTP requests to the appropriate URLs.


