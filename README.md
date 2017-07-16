# CMSC495 Chatbot
A (somewhat) simple Chatbot for Slack backed by a Recurrent Neural Network(RNN).

## Dependencies
- Python 3.6
- TensorFlow 0.12
- Numpy
- SciPy
- Six
- Slackbot
- NLTK (punkt, a NLTK library, is also required. See `punkt_dl.py` script in repo)

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

## Using the Docker Image as a production environment
### Building the Docker image locally with the Dockerfile

1. Installing Docker is outside the scope of this repository, please see here for more information: https://docs.docker.com/engine/installation/
2. Clone this repository
3. Open a terminal (BASH or PowerShell depending on environment), and navigate to the repository directory
4. Build the container using the following command: `docker build -t cmsc495:chatbot .`
5. Run the container using the following command: `docker run -m 2g -p 80:80 -p 443:443 -e "SLACKBOT_API_TOKEN=<Your token from step 2 here>" cmsc495:chatbot`



