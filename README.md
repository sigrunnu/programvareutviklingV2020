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
- [The release process](#the-release-process)
- [License](#license)

## Motivation

Due to the recent years with heavy focus on health and fitness, people are
now more than ever exercising. Instagram is overflowing of well-trained bodies,
but for many beginners it is hard to know where to start, and find out
which type of exercise which will give the best results.

Exercise It! aims to make it more accessible for the everyday man to start
exercising. Our application accomplishes this by letting users post and
share exercises with each other. This way it will be easier for everyone to
start exercising, no matter what starting point they have.

## How to use

[Click here](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/wikis/Leveranse-7/Brukermanual) for a detailed guide on how to use Exercise It!

## Code style

[Pep8](https://www.python.org/dev/peps/pep-0008/) is used to ensure that code
is tidy and consistent. Pep8 is checked in the CI pipeline on every commit. For more information about contribution, see [How to contribute](#how-to-contribute)

## Setting up a development environment

To make Exercise It! as accessible as possible, we want to make it easy for you to contribute to the project. In order to do that, there are several ways you can set up a development environment.

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
 You can now go to localhost:8000 and explore Exercise It!

</details>
  
 
<details>
  <summary>Click here to set up a development environment using MacOS</summary>
 
### Prerequisites

The following section assumes that you have a working installation of **Python 3.8** with PIP

If you don't have Python installed, follow [this installation guide](https://docs.python-guide.org/starting/install3/osx/)

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
 You can now go to localhost:8000 and explore Exercise It!

</details>
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


## Tech/framework used

Exercise It! is built with:

- [Django](https://www.djangoproject.com/)
- [Elasticsearch](https://www.elastic.co/)
- [Bootstrap](https://getbootstrap.com/)

## Tests and coverage
We are using [Pytest](https://docs.pytest.org/en/latest/) for testing. 

To run these tests, type:

```
pytest
```

To determine the code coverage, type:

```
pytest --cov
```

A folder named "*htmlcov* is then created in the 64 root folder. This folder contains html representations of all code coverage.

## How to contribute
Contributions to Exercise It! generally comes in the form of merge requests.  These are done by doing local changes. You can either create your own merge requests, make comments on or suggest changes to merge requests made by other developers. This is made possible by our open source policy, which makes existing merge requests, as well as the abillity to create new ones, open for everyone. Access the merge requests [here](https://gitlab.stud.iie.ntnu.no/tdt4140-2020/64/-/merge_requests).

<div align="center">
      <img src="http://134.209.236.146/static/Sketch-til-PU-Diagram-Page-11.png" alt="">
</div>


The process off proposing a change to Exercise It! can be summarized as follows (see the figure above):
  1. New functionallity will be added as GitLab issues. Choose the issue on which you want to contribute. Create a branch from **development**. Make sure you follow the naming conventions stated in the [GitLab Wiki](https://gitlab.stud.iie.ntnu.no/tdt4140-2020/64/-/wikis/Home/Git-&-GitLab-101) and the statndards for [code style](#code-style). 
  2. When the change is finished, create a merge request from your branch into the **development** branch. Write a summary of your code, including a plan on how it should be tested. Fix changes other developers have suggested to your merge request, if any.
  3. The development team will analyze your merge request and either merge or reject your request. If the merge request is rejected, it will be justified by.  
  4. If your merge request is accepted, your code will be added in the next release. See [release process](#the-release-process)

Please visit the [Evolusjon ](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/wikis/Leveranse-7/Evolusjon) wiki for futher reading about contribution to Exercise It!.

## The release process
The release process for Exercise It! can be summarized as follows:
  1. All code is developed on a separate branch and runs through a series of tests in a Continous Integration (CI) pipeline on every commit.
  2. Finished code is merged into the **development** branch through merge requests. The CI pipeline runs on every merge request.
  3. By the end of each sprint, the **development** branch is merged into master, which makes sure that all code developed in the current sprint is merged into master in one single merge request.
  4. When all the code is up and running in master, and the CI pipeline indicates that the tests are passing, the development team logs into the Digital Ocean server through SSH. This is done in the terminal. A ```git pull``` command is then run to fetch the recently merged code, from the master branch in the gitlab repository. If any modifications has been done to the models, these has to be migrated to the Production database from the server. Finally, Nginx is restarted to detect the changes. Now the new changes are released.

## License

Exercise It! is MIT licensed, as found in the [LICENSE](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE) file.
