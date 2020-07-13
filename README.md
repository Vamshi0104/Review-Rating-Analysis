# Review-Rating Analysis
Review-Rating Analysis through FLASK
----------------------------------------------------------------
Hey,user if you have idea about FLASK feel free to skip the below section or just have a look. 
#####  FLASK:
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
### Working of this Application :
Firstly the Application is Command line based executable under Python Environment and
uses popular Python micro web framework that is FLASK.This Application consist of 2 main pages runs in LocalHost wherein intially a form is given to the user based on the details entered and on submit by the user,Accordingly the Rating and Review is analyzed with support and importing of some python packages.This data is exported to Excel sheet there by the analysis can be done in efficient way.

##### Basically This project comprises of Three Modules :
* Index Page
* Review-Rating Analysis
* Exporting Form-Data

### Software Requirements:
* #####  Python 3+ any version or editors like Pycharm(Used in creating this application in Windows) 
* ##### Install Python Libraries as follows ,
 Run the these Commands in the Pycharm (venv) or CMD(for Windows) :

* For installing FLASK,follow the below link  as follows:
    ##### >>> Click to view documentation for [Flask-Install](https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba)


* For Review Analysis,importing vadersentiment is required ,thus run the command as follows:
>         pip install vaderSentiment

* For exporting the data from form to Excel ,thus run the command as follows:
>            pip install openpyxl

*  After installing above libraries,we need to import those and use the functionality in this application.

#### In order to run and intialize the application there are 2 alternative methods :

* Method - 1 : Run from Editor in venv and view localhost application in any Browswer with link (http://127.0.0.1:5000/)
* Method - 2 : Run from command prompt with specified path location of project by using following command
>            python __init__.py

## Output  
* Intro-Page :

 ![](Output_Intro-Page.png)

* Review-Rating form: 

![](Output_Review-Rating-form.png)

### Note : 
Here the file is named as init.py can be renamed as necessary changes should be made after in the above command before execution,The Output of Application can be viewed in Screenshots folder merged to this repo. 


>              Happy Coding :)
