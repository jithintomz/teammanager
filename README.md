Teammanager: CRUD api for managing team
=========================

Setup
------------

Install requirements

    $ sudo pip install -r requirements.txt

Run migrations

    $  python manage.py migrate

Run tests

    $  python manage.py test

Start development server

    $ python manage.py runserver

BasicUsage
------------

    # List all members
    
    curl -H 'Accept: application/json;  http://127.0.0.1:8000/api/members/
    
    # Add a member
    curl -X POST \
          
          http://localhost:8000/api/members/ \
          -H 'cache-control: no-cache' \
          -H 'content-type: application/json' \
          -d '{
            "first_name": "Jane",
            "last_name": "Doe",
            "phoneno": "8281958680",
            "email": "janedoe1@gmail.com",
            "role": "Regular"
        }'
        {"id":9,"first_name":"Jane","last_name":"Doe","phoneno":"8281958680","email":"janedoe1@gmail.com","role":"Regular"}
        
     # Edit member
      
      curl -X PATCH \
        http://localhost:8000/api/members/9/ \
        -H 'cache-control: no-cache' \
        -H 'content-type: application/json' \
        -d '{
          "first_name": "Jane",
          "last_name": "Doe",
          "phoneno": "+918281958680",
          "email": "janedoe1@gmail.com",
          "role": "Regular"
      }'
      
      {"id":9,"first_name":"Jane","last_name":"Doe","phoneno":"8281958680","email":"janedoe1@gmail.com","role":"Regular"}
      
    
