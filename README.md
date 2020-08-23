# Thought-works-project

Project Name: Market Place

Project Overview:It is a web application.It enables the users or customers to buy goods through online.For instance,
Amazon.com,Ebay.com


Clone my project: git clone https://github.com/Thilagavathycse/Thought-works-project.git


Installation instructions:

    Open a terminal or command prompt
    Navigate to the folder with your requirements.txt
    run: pip install -r requirements.txt
    You can install  all the dependencies

List of files: 
                                                                   
                                                                   Resource Api                           method                    
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

        filename:database.py
        username:""
        password:""
        host:localhost
        port:5432
        database:online_shopping
        
        
 Run description:
       run main.py
       
Known bugs:
working on generating hash for the password in database 
              