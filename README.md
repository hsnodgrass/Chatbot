# CMSC495 Chatbot
A (somewhat) simple Chatbot for Slack backed by a Recurrent Neural Network(RNN).

## Dependencies
- Python 3.6
- TensorFlow 0.12
- Numpy
- SciPy
- Six
- Slackbot
- NLTK

The program is run in a Python virtual environment for Python 3.5, which is included in the `venv` directory.

## Running the Program
*This section assumes you are using CentOS 7*
1. Clone this repo
2. Create a Slack chatbot integration. Add the bot user to whatever Slack channel you would like. Take note of the `Bot User OAuth Access Token`.
3. Copy the `slackbot_settings_template.py` to `slackbot_settings.py` in the same directory. Edit `slackbot_settings.py` and add your API token, and what channel you would like errors sent to, if any.
4. Gather all dependencies
  - To install Python 3.6, see here: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7
  - To install TensorFlow, see here: https://gist.github.com/87170360/0d445ae4100c2686067ee56901b42f9b
  - All other dependencies are installed using Pip, Python's package manager
5. Copy the `slack_integration` directory from the repo to your Python distribution's `site-packages` directory. Typically `/usr/lib/python3.5/site-packages/`
6. `cd` to the repo, and run `venv/tensorflow/bin/python3.5 run.py`

## Using the Docker Image as a testing environment
*These instructions are Linux specific, but the work-flow can be transposed onto other environments.*
### Building the Docker image locally with the Dockerfile

1. Verify that docker is installed and running non your system. 
-- Use the standard Docker "hello world" test.
```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
...(snipped)...
```
2. Download only the Dockerfile and the REQUIREMENTS files. 
```bash
$ wget https://raw.githubusercontent.com/CMSC495-Summer2017/Chatbot/master/Docker/Dockerfile
$ wget https://raw.githubusercontent.com/CMSC495-Summer2017/Chatbot/master/Docker/REQUIREMENTS
```
3. Build the image in the directory where you downloaded the files in step 2.
```bash
$ docker build -t bot-testing .
docker build -t bot-testing .
Sending build context to Docker daemon  1.175GB
Step 1/7 : FROM hoverbear/archlinux
 ---> 76cc92d512c3
Step 2/7 : ADD REQUIREMENTS /
 ---> 9bdb33b16e18
Removing intermediate container 2cf4d07844e1
Step 3/7 : RUN pacman -Syu --noconfirm --force
 ---> Running in 54840b583c9b
:: Synchronizing package databases...
downloading core.db...
downloading core.db...
downloading core.db...
downloading core.db...
downloading core.db...
downloading extra.db...
downloading extra.db...
downloading extra.db...
...(snipped)...
Successfully tagged bot-testing:latest
```
4. Run the docker image in the "source" directory. (The directory where you either cloned the entire
   repo or where your own .py files are)
```bash
docker run -t -i --rm=true -v $(pwd):/source archtest /bin/bash
```
5. You will be dropped into a shell inside your new container. 
--* If you are running the test_bot.py you will need to edit the slackbot_settings_template.py file
(or your local equivelent) and add the API_TOKEN. Vim has been installed into the image for this
purpose. 
--* You can modify the Dockerfile to include another editor if you prefer (ie nano or emacs).
-- The container does not support GUI based editors.

6. From this point, you can run the .py files as you would on your own system. 

###Use pre-built docker image.
1. Download just the Docker image 
```bash
$ wget
https://raw.githubusercontent.com/CMSC495-Summer2017/Chatbot/master/Docker/bot-testing.latest.tar
```
2. Import the docker image 
```bash
docker load -i bot-testing.latest.tar
```
3. Change directories to your source directory. Then follow stesps 4-6 from section above. 



