# EXAMPLE OF BASIC AUTH USING DJANGO AND BCRYPT
---

### Using this example app, you can make AJAX requests in the following ways:

- GET request to 'api/useraccount' that will return all users in the db

- POST request to 'api/useraccount' that will add a new user to the db.    
        - Requires an email and password field.
        - Email must be unique.
        - Password will be hashed using bcrypt prior to being stored in db.

- GET request to 'api/useraccount/{userId}' that will return a single user from the db

- PUT request to 'api/useraccount/{userId}' that will update a single user
        - Password revisions will be hashed prior to being put in the db.
        - Both email and password must be sent in request.

- DELETE request to 'api/useraccount/{userId}' that will delete one user

- GET request to 'api/useraccount/login' that will return an empty object

- PUT request to 'api/useraccount/login' that will find a user in the db by their email and compare their hashed password to the password in the request.
          - If they match, a user object will be returned that contains the user email and id but not the password.
          - If they do not match, an empty object will be returned.
          - If the user email does not exist in the db, an empty object will also be returned.


---
#### All responses will be sent in JSON format.
