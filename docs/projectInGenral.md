## First you should install the project


```
$ git clone https://github.com/AlMonther9/ZSI.git
$ python3 -m venv .venv
```

> [!NOTE]
> If you are on windows os Use `python` instead of `python3`

### For windows 
```
$ venv\bin\Activate.ps1
```
### For linux
```
$ source venv/bin/activate
```
### Install all the pkgs
```
(venv) $ pip install -r requirements.txt
```
And you will also need download [Mysql officail website](https://www.mysql.com/downloads/)<br>
Or<br>
You can use sqlite3 instead <br>check `settings.md` for more info before run the server 
### Now you can run the server 
```
(venv) $ flask run
``` 

## For more details 
`settings.md` for change databse config ,server address and port <br><br>
`models.md` for change ORM logic<br><br>
`views.py` for write your apis and configure it <br>
