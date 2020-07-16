# at-summer-automated-tests:
This is a project to show my vision on how 5 hours automated framework could looks like

# Setup
1. git clone `https://github.com/sebawo/at-summer.git`
2. download remote branch and switch to it `git checkout --track origin/2019_07_01_andrei_talashka_solution`
3. goto `config.json.example` and add actual passwords for all tested environments (security requirements)
4. use `cp config.json.example config.json` to rename config file

# Command line Execution:
1. navigate to project directory
2. run docker container `docker-compose build` and `docker-compose up -d`
3. open at-summer_summer_1 container terminal (one option is to use Kinematic -> at-summer_summer_1 -> execute)
4. type in docker terminal to run pipenv shell `pipenv shell`
5. type in docker terminal to run tests `python -m test_runner`

# Test result screen shot:
![Screenshot](screenshot.png)
