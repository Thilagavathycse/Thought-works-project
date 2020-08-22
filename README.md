# Thought-works-project
Project Name: Market Place
Project Overview:It is a web application.It enables the users or customers to buy goods through online.For instance,
Amazon.com,Ebay.com
Clone my project: git clone https://github.com/Thilagavathycse/Thought-works-project.git
Installation instructions:
         1.Python editor
         2.installation command for cmd:pip install flask.
           Flask 1.1.2
           Werkzeug 1.0.1
         3.install all the packages mentioned in requirements.txt
           command for cmd:pip install package name
List of files:                                                                    Resource Api             HTTP method                    
        1.database.py  #Database connection
        2.login.py     #For User login                                  http://127.0.0.1:5000/user           POST
        3.app.py       #jwt token file                                  
        4.categories   #To display categories                           http://127.0.0.1:5000/categories      GET
                                                                        http://127.0.0.1:5000/<category_id>   GET
        5.items.py     #To get item details                             http://127.0.0.1:5000/<id>            GET
        6.carts.py     #Add to cart                                     http://127.0.0.1:5000/cart            POST
                       #update item in cart                             http://127.0.0.1:5000/cart            PUT
                       #Delete item from cart                           http://127.0.0.1:5000/cart            DELETE
                       #View items                                      http://127.0.0.1:5000/cart            GET
        7.main.py      #To run all the files
Database Configuration:
        server:localhost http://127.0.0.1:5000
        Server :localhost
        Database :online_shopping
        Port :5432
        Username :postgres
        Password for user postgres:#Thilaga1094
 Run description:
       run main.py
Known bugs:working on generating hash for the password in database 
              