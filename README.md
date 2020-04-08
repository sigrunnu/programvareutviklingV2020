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

### Step 2: Build the Docker Image

### Step 3: Verify your Docker Machine IP address

### Step 4: Run the Docker Container

  </details>
<details>
  <summary>Click here to set up a development environment using the Windows OS</summary>
  
  ### Prerequisites
  ### Step 1: Clone the repository from GitLab
  ### Step 2: Install the required packages
  ### Step 3: Run the Django server locally

</details>
<details>
  <summary>Click here to set up a development environment using MacOS</summary>
  
  ## Prerequisites

  You will need Python 3.8 for this project

  **Option 1 (beginner friendly)**

  Visit [the official Python download page](https://www.python.org/downloads/)

  **Option 2 (advanced)**

  Make sure [Homebrew](https://brew.sh/index_nb) is installed

  Install Python 3.8 by typing

  ```
  brew install python@3.8
  ```

  Add the newly added Python installation to path using 

  ```
  echo 'export PATH="/usr/local/Cellar/python@3.8/3.8.2/libexec/bin:$PATH"' >> ~/.bash_profile
  ```

  ### Step 1: Clone the repository from GitLab

  
  
  Either clone with SSH (SSH keys needs to be configured)
  ```cmd
  git clone git@gitlab.stud.idi.ntnu.no:tdt4140-2020/64.git
  ```

  or clone with HTTPS
  ```
  git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64.git
  ```
  
  ### Step 2: Install the required packages

  Exercise It! use a bunch of Python packages to ensure seamless development

  Install the required packages by typing

  ```
  pip install -r requirements.txt
  ```

  and

  ```
  pip install -r requirements-ci.txt
  ```

  Please note that you have to run both commands

  
  **Make sure you point to the correct Python installation!**
  
  By default on MacOS, the pre-installed Python 2.7 that comes with every mac, is the version that ```python``` points to. This means that you might have to replace ```pip``` with ```pip3```, or the packages will be installed for Python 2.7 version, if you did not configure an alias correctly. 

  ### Step 3: Run the Django server locally

  To run the server type

  ```
  python3 manage.py runserver
  ```

  or if you managed to set up an alias

  ```
  python manage.py runserver
  ```
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
4. Submit a pull request with a comprehensive list of changes made 📝

We will review your changes and hopefully they will take a part of the project

## License

Exercise It! is MIT licensed, as found in the [LICENSE](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE) file.
