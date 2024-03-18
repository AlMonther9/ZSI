## welcome to models

#### first i want to explain to you what's ORM (Object Relation Mapping)
  An ORM tool is software designed to help OOP developers interact with relational database without write and queries to your database its more secure and more easy you will not need to write pure query usually
  in our case we will use `flask-sqlalchemy`

### so lets know how we can add or drop tables and columns 
``` python
class RealTimeCoordinates(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude =db.Column(db.Float, nullable=False)
    altitude = db.Column(db.Float, nullable=False)
    google_maps = db.Column(db.Float)
    DataTime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    air_quality_id = db.Column(db.Integer, db.ForeignKey("air_quality.id"))
```

in this example you have a table named `real_time_coordinates` cause our class name is RealTimeCoordinates so flask_alchemy create a table in our data base with lowercase letters and "_" after every single word "snake_case"
<br>if we want a new table we will easily write a class and it will inherit from db.Model class

``` python
class NewTable(db.Model):
  pass
```
make sure you write class name in "PascalCase" , next lets add some fields in it 
``` python
class NewTable(db.Model):
  first_field = db.Column(db.Integer)
```
you add fields easily as you see and specifiy the data type that you should store in it with db. if you want to know more about fields and model in flask-sqlalchemy you can read the [docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
To ease my conscience that the old way there are a new way bit it's so complex to handle you can check out it in the [new doc](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/models/) 
i hope every class you implement add in it an id field
``` python
class NewTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_field = db.Column(db.Integer)
```
its always a primary key by the way. i think now you can edit your tables easily  but what's this relationship field that i wrote it in AirQuality class? you can can find out what's relationships in sql databases and know [what are these](https://blog.devart.com/types-of-relationships-in-sql-server-database.html)
then you can know who [we can implement them in sqlalcemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships) 

### what after make your changes ?
you should migrate your changes with database and its very very simple watch :
```
(venv) $ flask db migrate -m "comment with your changes"
(venv) $ flask db upgrade
```
 have a nice day :) 
