**Conda Environment**
1. Make sure you install Miniconda
2. You can  start conda using : **source ~/miniconda3/bin/activate**
3. Create a new environment using **conda create -n mini_rag python=3.8**
4. to activate environment  **conda activate mini_rag**

**git ignore**
1. You can find templates for git ignore here : https://github.com/github/gitignore/blob/main/Python.gitignore

**Licence**
1. You should have a licence in your project

**Fast api**
1. You need uvicorn with it
2. To start a server use **uvicorn main:app --reload --host 0.0.0.0 --port 5000**
3. you can go to documentation through **http://localhost:5000/docs**
4. We will set up multiple routes in routes folder , and include them in our main 
5. we load env variables in our system first before including the routes

**Pydantic**
- Used for datatype validation (**pydantic-settings**)
- We will mainly use it to validate and load .env 
- We will also use it for any other datatype validation we need

**FastAPI Depends Module**
``` python
@app.get("/items/")
async def read_items(query_params: dict = Depends(get_query_params)):
    return query_params
```
When a request is made to /items/, FastAPI calls get_query_params, extracts the query parameters, and passes the result to read_items.

**Enums**
- Enums are basically used to store constans in our project
``` python
from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
```

**__init__**
- very helpful when you have muultiple files in one directory for importing 
Example : 
```
project/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
```
- without __init__ 
To import User model from the models package, you would need to write
``` python
from app.models.user import User
```

- with __init__
By adding an  __init__.py file  you can simplify imports:
```python
from app.models import User
```
after adjustin the __init__.py file

**OS Pathes**
In Python, the os.path module provides a set of functions for working with file and directory paths
when joinin pathes it`s recomended to use the functions provided by os to avoid linux and windows issues
``` py 
import os

base_path = "C:/Users/YourName"
file_name = "document.txt"

full_path = os.path.join(base_path, file_name)
print(full_path)  # Output: C:/Users/YourName/document.txt
```

**files in web apps**
- to load files uploaded it`s recommended to load it in chunks 
- best library to deal with files is aiofiles

