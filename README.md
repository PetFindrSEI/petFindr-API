# [Petfindr API](https://petfindr-api.herokuapp.com/pets/)

## Project Description

The PetFindr API contains all information needed for pets or users. The pets model offers a detailed look at multiple parameters needed to search for a specific lost/found pet. This API was built with Django and PostgreSQL and deployed with Heroku. Photo storage is handled by AWS using an S3 bucket. 

## Technologies Used

- Python
- Django
- Django Rest Framework
- Djoser
- AWS S3
- AWS IAM

## Installation Instructions

To install this repository:

- If you would like to fork the repository so you have your own copy, feel free to!
- Click on the green "Code" button.
- Copy either the HTTPS or SSH link that is provided (SSH is preferred)
- Open up the Terminal and navigate to the desired directory location
- Once inside, use the code "`git clone` copied_link_here"
- Once the repo has been installed, change into the directory with `cd petFindr-API`
- From here you can run `code .` to open it up in VS Code


## Models

User Model:
```js
    {
        "id": 1,
        "email": "petfindr@petfindr.com",
        "username": "petfindr",
        "avatar": ""
    }
```

Pet Model:
```js
    {
        "id": 10,
        "status": "Found",
        "name": "Thor",
        "type": "Dog",
        "gender": "M",
        "size": "L",
        "color": "Golden",
        "description": "Somehow he carries a Giant hammer with him everywhere he goes.",
        "microchip": "Y",
        "location": "Space",
        "created_at": "2022-02-14T17:30:52.723091Z",
        "reported_time": "2026-07-14T11:30:00Z",
        "owner": "petfindr",
        "photo": "https://petfindr.s3.amazonaws.com/images/default.jpg",
        "phone_number": "1234567890",
        "owner_email": "petfindr@petfindr.com"
    }
```

## Django REST Framework

From inside the Django REST framework, you can perform all CRUD operations on any pet that is connected with your account. You can also alter your user info from the `users/me/` endpoint. 

## Endpoints

- Default: https://petfindr-api.herokuapp.com/
- View All Pets: https://petfindr-api.herokuapp.com/pets/
- View Specific Pet (By ID): https://petfindr-api.herokuapp.com/pets/37
- View Current User: https://petfindr-api.herokuapp.com/users/me/



## Major Hurdles / Unsolved Problems

### Unsolved Problems

- Would like to add additional parameters on the pets model for a more detailed search query

### Major Hurdles

- Setting up a default image in AWS was a hurdle, we tackled that by setting the default image in the pets `model.py` file, and then uploading an image through the Django REST framework with the same pathname so any time an object is uploaded without an image, it will default to the image that was initially uploaded. 
