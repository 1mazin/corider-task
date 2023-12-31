# Flask CRUD Application with MongoDB

This is a Flask application that allows you to perform CRUD operations (Create, Read, Update, Delete) on a User resource using a REST API. The application utilizes the Flask framework and the PyMongo library to connect to a MongoDB database.

## Steps to setup 

1. Clone this repository to your local machine:

2. Navigate to the project directory:

3. Create a virtual environment for the project:
    ```
    python -m venv venv
    ```
4. Activate the virtual environment.

5. Install all the required dependencies by using the command given below:

   ```
   pip install -r requirements.txt
   ```
6. To run
   ```
   python app.py
   ```

## Configuration

Before running the application, you need to configure the MongoDB connection settings. Open the `config.py` file and update the connectionString with you mongodb connection string.


## Build and Run with Docker

1. Build the Docker image:

```bash
docker build -t flask-mongodb-app .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 flask-mongodb-app
```

The application will be running on `http://localhost:5000`.


## API Endpoints

The following REST API endpoints are available:

- `GET /users`: Returns a list of all users.
- `GET /users/<id>`: Returns the user with the specified ID.
- `POST /users`: Creates a new user.
- `PUT /users/<id>`: Updates the user data with specified ID.
- `DELETE /users/<id>`: Deletes the user with the specified ID.

Use a tool like Postman to test the API endpoints by sending HTTP requests to the appropriate URLs.

Demo.mp4 demonstrates the application using Postman.


