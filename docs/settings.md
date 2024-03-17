## welcome to settings file 
I designed this file carfully to make it ez to change later SO.. <br>
You are here to :
- Configue Your mysql database <br>
- Use sqlite3  <br>
- Change servser address && Change Port <br>

if you want to do anything else contact with mekha or back to `projectInGenral.md`
## Configue Your mysql database
```python
DATABASE = {
    'user': 'your user name here',
    'pw': 'your password here',
    'db': 'database name',
    'host': 'the host of the databsse server',
    'port': 'Port of your database server its usually on 3306',
}
```
<p>
You will easily change the values to your own database configuration  <br>
You will put your user , password , databse name , host and port <br>
it's easy to get this info just make a little search or easy ask me :D  <br>
you will download mysql then
  
```
  $ mysql -u root -p 
```
you will enter your password you made before 
```
mysql> CREATE DATABASE db_name;
```
after that you will migrate your connect your project with database

```
mysql> exit
(venv) $ flask db init
(venv) $ flask db mograte -m "initial migrate"
(venv) $ flask db upgrade 
```
</p>

##  Use sqlite3 
if you are a lazy man i don't recommend use sqlite3 for many issues but anyway

```
(venv) $ pip install sqlite3
```
then you will update this lines like this 
``` python
# DB_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['pw']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['db']}"
DB_URL = f"sqlite:///db.sqlite3"
```
now you can make this commands
```
(venv) $ flask db init
(venv) $ flask db mograte -m "initial migrate"
(venv) $ flask db upgrade 
```

you will notice that a instance folder will be genrate and a db.sqlite3 file in it>

## Change servser address && Change Port
you ofcourse notice these lines 
``` python
SEREVER_ADDRESS = '0.0.0.0'
PORT = 3000
```
if you let them like that the server address will change dynamically so i recommend to make in constant address

