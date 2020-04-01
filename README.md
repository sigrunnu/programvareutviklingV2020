<div align="center">
      <a href="http://134.209.236.146">
        <img src="http://134.209.236.146/static/feed/logo.png" alt="Exercise-it Logo" width="72" height="72">
      </a>
</div>
<div align="center">
    <h3>Exercise-it</h3>
</div>
<div align="center">
  <strong>Build the foundation for your active life:</strong><br>
  Get inspiered and share exercises with Exercise-it
</div>
<br/>
<div align="center">
  <a href="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="Exercise-it is released under the MIT license." />
  </a>
  <a href="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/commits/master">
    <img src="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/badges/master/pipeline.svg" alt="Pipeline status"/>
  </a>
  <a href="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/commits/master">
    <img src="https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/badges/master/coverage.svg" alt="Coverage report"/>
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
      <strong>
  </a>
</div>
 
<br>

## Table of contents

- [How to use?](#how-to-use)
- [Set up a development environment](#setting-up-a-development-environment)
- [Tech/framework used](#techframework-used)
- [Tests and coverage](#tests-and-coverage)
- [License](#license)


## How to use?

For a detailed guide on how to use Exercise It!, please click here [](wiki/)

## Code style

[Pep8](https://www.python.org/dev/peps/pep-0008/) is used to ensure code 
is tidy and consistent. Since a Pep8 check is done in CI, you will need to 
follow the rules specified by this style guide, if you want to contribute.

## Setting up a development environment
To make ExerciseIT as accessible as possible, we want to make it easy for you to contribute to the project. In order to do that, there are several ways you can set up a development environment.

<details>
  <summary>Click here to set up a development environment using Docker</summary>

  ### What is Docker?
  Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications       from your infrastructure so you can deliver software quickly. ExerciseIT has features that allows it to run on Docker Toolbox.        Docker toolbox can be installed on both the Windows OS and MacOS. 

  Note that running ExerciseIT on Docker requires specific changes to the operating system of your computer. If you are new to software development and dont feel comfortable editing the settings of your operative system. You should consider the guide for setting up a development environment on Windows or MacOS.
  ### Prerequisites
  To run ExerciseIT on Docker, you need to have Docker Toolbox installed. To install Docker Toolbox, please visit the official Docker   installation Guide.
  - [**Install on Windows**](https://docs.docker.com/toolbox/toolbox_install_windows/)
  - [**Install on MacOS**](https://docs.docker.com/toolbox/toolbox_install_mac/)
  
  When you have completed the installation, and successfully run the ```docker run hello-world``` command, proceed to the next step.
  ### Step 1: Clone the repo from GitLab
  ### Step 2: Build the Docker Image
  ### Step 3: Verify your Docker Machine IP adress
  ### Step 4: Run the Docker Container
  </details>
<details>
  <summary>Click here to set up a development environment using the Windows OS</summary>
  
  ### Prerequisites
  ### Step 1: Clone the repo from GitLab
  ### Step 2: Install the requirered packages
  ### Step 3: Run the Django server locally

</details>
<details>
  <summary>Click here to set up a development environment using MacOS</summary>
  
  ## Prerequisites
  ### Step 1: Clone the repo from GitLab
  ### Step 2: Install the requirered packages
  ### Step 3: Run the Django server locally
</details>

## Tech/framework used

Exercise is built with
- [Django](https://www.djangoproject.com/)
- [Elasticsearch](https://www.elastic.co/)
- [Bootstrap](https://getbootstrap.com/)

## Tests and coverage
Describe and show how to run the tests with code examples.

To run tests, type:
```
pytest
```

To determine code coverage, type: 
```
pytest --cov
```

## License
Exercise-it is MIT licensed, as found in the
[LICENSE](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/64/-/blob/master/LICENCE) file.
