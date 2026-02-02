# REST API WEBSERVER (PYTHON + FLASK FRAMEWORK)

## I. PROJECT INITIALIZATION

### 1. UBUNTU SERVER

**Install and Setup ubuntu machine**
  - with `USERNAME` & `PASSWORD`
  - DISK - 30 GB
  - MEMORY - (8-9)GB
  - CPU - 4

**Verify the Setup**

```sh
# DISK SPACE
  df -h

# DISK USAGE
  du -sh < folder_name > 

# MEMORY USAGE
  free -h

# USER AND GROUP DETAILS
  cat /etc/passwd | grep < username >
  cat /etc/group | grep < username >
```

### 2. PREREQUISITES TOOLS
```sh
#.......... INSTALLATION COMMANDS ..........

# python:3.12 
  sudo apt update && sudo apt install python3
  python3 --version

# git
  sudo apt update && sudo apt install git
  git --version

# pip
  sudo apt update && sudo apt install pip
  pip --version

# .......... VERIFY INSTALLED PACKAGES ..........

# USE Debian Package Manager / APT
  dpkg -l | grep "git"
  apt list --installed | grep "git"

```

## II. INSTALLATION OF LIBRARIES

### 1. PYTHON VIRTUAL ENVIRONMENT SETUP

- Once after setting up all the project prerequisites, if we do `pip install flask` throws `ERROR` because:
  - FLASK isn't a `Debian Package`, Its a `Python Library` !!!
  - To install Python packages we need a `Python Virtual Environment`

  ```py
  # Command to Setup Python Vitual Environment
    sudo apt update && sudo apt install python3.12-venv

  # Enable Python Virtual Environment Folder
    python3 -m venv venv

  # Activate the Python Virtual Environment
    source venv/bin/activate  # This command activates the VENV W.R.T venv folder
  ```
---

### 2. INSTALL PYTHON LIBRARIES IN VENV

  ```sh
  # Install all the required Libraries
    pip install flask sqlalchemy dotenv psycopg2-binary flask-migrate

  # List all the Installed Packages
    pip list

  # Store the Installed Packages details in a file named requirements.txt
    pip freeze > requirements.txt
  ```

## 3. POSTGRESQL SERVICE SETUP IN LOCAL

### 1. INSTALL POSTGRES SERVICE
  
  ```sh
  # Install Postgresql 
    sudo apt update && sudo apt install postgresql postgresql-contrib

  # Verify Installation
    sudo systemctl status postgresql
  
  # To Start Postgresql Service
    sudo systemctl start postgresql
  
  # To Enable Postgresql Service
    sudo systemctl enable postgresql

  # Verify Processes of Postgresql Service
    ps aux | grep 'postgresql'
  ```

### 2. POSTGRESQL DATABASE CONFIGURATION

  ```sql
  -- Connect to Postgresql Shell
    sudo -u postgres psql  -- [Default:- User: postgres; Shell: psql]
  
  -- Create a User with Password and Verify
    CREATE USER user01 WITH PASSWORD `user@123`;

  -- Alter the Password for an existing User if needed
    ALTER USER user01 WITH PASSWORD `< new_password >`;

  -- Create a Database
    CREATE DATABASE studentdb;

  -- Grant Previleges to User for DB
    GRANT ALL PRIVILEGES ON DATABASE studentdb TO user01;

  -- Change the Ownership for the DB
    ALTER DATABASE studentdb OWNER TO user01;

  -- Delete a User
    DROP USER user02;

  -- Exit the Shell
    exit

  -- Connect the Shell with the New User
    psql -U user01 -d studentdb -h localhost -W;

  -- List all Users from outside
    sudo -u postgres psql -c "\du"

  -- List all Databases from outside
    sudo -u postgres psql -c "\l"
    ```
