<div align="center">
      <a href="http://134.209.236.146">
        <img src="http://134.209.236.146/static/feed/logo.png" alt="Exercise It! Logo" width="100" height="100">
      </a>
</div>
<div align="center">
    <h3>Exercise It!</h3>
</div>
<div align="center">
  <strong>Build the foundation for your active life:</strong><br>
  Get inspired and share exercises with Exercise It!
</div>
<br/>
<div align="center">
  <a href="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="Exercise It! is released under the MIT license." />
  </a>
  <a href="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/commits/master">
    <img src="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/badges/master/pipeline.svg" alt="Pipeline status"/>
  </a>
  <a href="https://www.python.org/dev/peps/pep-0008/">
    <img src="https://img.shields.io/badge/code%20style-pep8-orange.svg" alt="Coverage report"/>
  </a>
</div>

<br>
 
<div align="center">
  <a href="http://134.209.236.146">
      <strong>
        Try out Exercise It!
      </strong>
  </a>
</div>
 
<br>

## Table of contents

- [Motivation](#motivation)
- [How to use](#how-to-use)
- [Set up a development environment](#setting-up-a-development-environment)
- [Tech/framework used](#techframework-used)
- [Tests and coverage](#tests-and-coverage)
- [How to contribute](#how-to-contribute)
- [License](#license)

## Motivation

Due to the recent years heavy focus on health and fitness, people are
now more than ever exercising. Instagram is overflowing of well trained bodies,
but for many beginners it is hard to know where to start, and find out
which type of exercise which will give the most effect.

Exercise It! aims to make it more accessible for the everyday man to get
into exercising. Our application accomplishes this by letting users post and
share exercises with each other. This way it will be easier for everyone to
start exercising, no matter what starting point.

## How to use

[Click here]() for a detailed guide on how to use Exercise It!

## Code style

[Pep8](https://www.python.org/dev/peps/pep-0008/) is used to ensure code
is tidy and consistent. Since a Pep8 check is done in CI, you will need to
follow the rules specified by this style guide, if you want to contribute.

## Setting up a development environment

To make Exercise It! as accessible as possible, we want to make it easy for you to contribute to the project. In order to do that, there are several ways you can set up a development environment.

<details>
  <summary>Click here to set up a development environment using Docker</summary>

### What is Docker?

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. Exercise It! has features that allows it to run on Docker Toolbox. Docker toolbox can be installed on both the Windows OS and MacOS.

Note that running Exercise It! on Docker requires specific changes to the operating system of your computer. If you are new to software development and dont feel comfortable editing the settings of your operative system. You should consider the guide for setting up a development environment on Windows or MacOS.

### Prerequisites

To run Exercise It! on Docker, you need to have Docker Toolbox installed. To install Docker Toolbox, please visit the official Docker installation Guide.

- [**Install on Windows**](https://docs.docker.com/toolbox/toolbox_install_windows/)
- [**Install on MacOS**](https://docs.docker.com/toolbox/toolbox_install_mac/)

When you have completed the installation, and successfully run the `docker run hello-world` command, proceed to the next step.

### Step 1: Clone the repository from GitLab
Open your terminal and navigate to the folder in which you will clone the project. In this folder, run the following command:
```
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64.git
```
When the cloning is finished, navigate inside the repo with 
```
cd 64
```
When you are inside the repo and the teminal looks something like this:
```
C:\Users\<Username>\<Coding_projects>\64>
```
proceed to the next step.
### Step 2: Build the Docker container
Now you need to build the docker container.This is done bu using Docker Compose, which is a tool for defining and running Docker applications. The configurations for the Docker container is found in the Dockerfile and in docker-compose.yml. To build the container, simply run:
```
docker-compose build --no-cache
```
The output should be something like this:
```
Building web
Step 1/7 : FROM python:3
 ---> f88b2f81f83a
Step 2/7 : ENV PYTHONUNBUFFERED 1
 ---> Using cache
 ---> f37beef4faa5
Step 3/7 : RUN mkdir /code
 ---> Using cache
 ---> 8986058c087d
Step 4/7 : WORKDIR /code
 ---> Using cache
 ---> e322d7f36b34
Step 5/7 : COPY requirements.txt /code/
 ---> Using cache
 ---> 1a3188355137
Step 6/7 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 7105abaa6f6d
Step 7/7 : COPY . /code/
 ---> 9df05e8285ca
Successfully built 9df05e8285ca
Successfully tagged 64_web:latest
```
when successfully created the docker image, proceed to the next step.
### Step 3: Verify your Docker Machine IP address
Docker Machine is a tool for provisioning and managing your Dockerized hosts (hosts with Docker Engine on them). You can view Docker Machine as a server that runs the project. The default Docker machine was created when you installed Docker Toolbox. The default ip adress for this server is: 192.168.99.100. To verify this, run:
```
docker-machine ls
```
from the 64 project repo. The output should be something like this:
```
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER     ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v19.03.5
```
If the URL shows a different IP-adress (tcp:// different ip adress :2376), you should use this IP adress when running the Exercise It! projects locally on your computer.
### Step 4: Run the Docker Container
Now all is set for running the Exercise It! repo with Docker. To start the Docker Container, simply run the following copmmand:
```
docker-compose up
``` 
make sure you are in the 64-folder when running this command. 

You if you see no errors you should now be able to se the procject running on the IP adress of your docker machine at port 8000. If you have the default IP-adress: 192.168.99.100. You can write 192.168.99.100:8000 in the web browser and explore the Exercise It! project. If not, use the ip adress you fond in step 3.

### Running commands
To run commands in the Docker application, open up a new terminal window and write (in the 64-folder):
```
docker-compose run web "your command here" 
```

For example, you may run the tests for the projects with:
```
docker-compose run web pytest feed/ search_indexes/ profile_page/
```

To run the migration files, you can run the following command:
```
docker-compose run web python manage.py migrate
```
### Encountering errors
If you encounbter network errors, you may need to restart your Docker Machine. To do this write the following commands:
```
docker-machine stop
docker-machine start
docker-machine env
```

After restarting the docker machine, you must verify the IP-adress again.
  </details>
<details>
  <summary>Click here to set up a development environment using the Windows OS</summary>
  
### Prerequisites

The following section assumes that you have a working installation of **Python 3.8** with PIP

If you don't have Python installed, follow [this installation guide](https://docs.python-guide.org/starting/install3/win/)

### Step 1: Clone the repository from GitLab

Open a terminal and navigate to the folder in which you will clone the Exercise IT! repo. Then, clone the repo with HTTPS

```
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64.git
```

### Step 2: Install the required packages

Exercise It! use a bunch of Python packages to ensure seamless development

**Make sure you point to the correct Python installation**
If you installed python 3 with Chocolatey, python 3 will be pushed as the default python version. Thus by writing ```python --version``` in your command line, you should see something like this:
```
C:\Users\"username">python --version
Python 3.8.1
```
The python version should be at least 3.8

If instead you get python 2.* as a result, you should try running ```python3 --version```, if the you get ```python 3.8.*``` as a result, you are good to go. If not, try reeinstalling python 3.

Install the required packages by typing

```
pip install -r requirements.txt
```

and

```
pip install -r requirements-ci.txt
```

Please note that you have to run both commands

### Step 3: Run the Django server locally

To run the server type

```
python3 manage.py runserver
```

or if python 3 is the default version

```
python manage.py runserver
```
 You can now go to localhost:8000 and explore Exercise IT!

</details>
  
 
<details>
  <summary>Click here to set up a development environment using MacOS</summary>
 
### Prerequisites

The following section assumes that you have a working installation of **Python 3.8** with PIP

If you don't have Python installed, follow [this installation guide]()

### Step 1: Clone the repository from GitLab

Navigate to the folder you wold like to clone the repo to and type:

```
git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64.git
```

### Step 2: Install the required packages

Exercise It! use a bunch of Python packages to ensure seamless development

**Make sure you point to the correct Python installation**

By default on MacOS, the `pip` will point to the pre-installed Python 2.7 version, if no aliases is configured. Make sure to replace `pip` with `pip3` if you did not configure aliases, or packages will be installed for Python 2.7.

Install the required packages by typing

```
pip install -r requirements.txt
```

and

```
pip install -r requirements-ci.txt
```

Please note that you have to run both commands

### Step 3: Run the Django server locally

To run the server type

```
python3 manage.py runserver
```

or if you have managed to set up an alias, type:

```
python manage.py runserver
```
 You can now go to localhost:8000 and explore Exercise IT!

</details>


## Tech/framework used

Exercise It! is built with

- [Django](https://www.djangoproject.com/)
- [Elasticsearch](https://www.elastic.co/)
- [Bootstrap](https://getbootstrap.com/)

## Tests and coverage

To run tests, type:

```
pytest
```

To determine code coverage, type:

```
pytest --cov
```

## How to contribute

1. Follow the steps listed in [Set up a development environment](#setting-up-a-development-environment) section to get the project working on your machine
2. Create a branch
3. Make some changes 👨‍💻
4. Submit a merge request with a comprehensive list of changes made 📝

We will review your changes and hopefully they will take a part of the project

## License

Exercise It! is MIT licensed, as found in the [LICENSE](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE) file.
