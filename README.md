# Bus Times
this is an Alexa Skill that given a bus number it return the time countdown from my local bus stop (St Paul's Road / Ramsey Walk)

## Instructions
First we want to set the virtual environment. This is needed later when we want to deploy the application in AWS.

```bash
# install virtualenv
$ pip install virtualenv

# set virtualenv in your project directory
$ cd bus_times
$ virtualenv venv

# activate the virtual environment
$ source venv/bin/activate
```

We also need to install [flask-ask](https://github.com/johnwheeler/flask-ask) which is the library used to write the Alexa skills.

```bash
$ pip install flask-ask
```

once all the dependencies are installed we can run the application.

```bash
$ python bus_times.py
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  * Restarting with stat
```

## Test
Once the application is up and running we can either decide to test it locally and set up a tunnel or to deploy the application directly in AWS.

### Test Locally
Before create the Alexa Application we need to run a tunnel to allow the application to point to our local server.

We will use [ngrok](http://ngrok.com) which generates a temporary and valid `https` link that allow to expose our server.
```bash
$ ngrok https 5000

ngrok by @inconshreveable                         (Ctrl+C to quit)

Session Status                online
Version                       2.1.18
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://50e84cf8.ngrok.io -> localhos
Forwarding                    https://50e84cf8.ngrok.io -> localho

Connections                   ttl     opn     rt1     rt5     p50
                              0       0       0.00    0.00    0.00

```

### Deploy in AWS
In order to deploy the application in AWS we will be using [zappa](https://github.com/Miserlou/Zappa) which will interact with the AWS CLI to deploy the code.

here is how to do the installation

```bash
$ pip install zappa

$ zappa init

# deploy in AWS using the setting defined in zappa_settings.json
$ zappa deploy dev
Calling update for environment dev..
Downloading and installing dependencies..
 95%|███████████████████████████████████████████████████████████   | 40/42 [00:14<00:00,  2.27pkg/s]
Packaging project as zip..
Uploading bus-times-dev-1234567890.zip (7.9MiB)..
100%|███████████████████████████████████████████████████████████| 8.31M/8.31M [00:23<00:00, 217KB/s]
Updating Lambda function code..
Updating Lambda function configuration..
Uploading bus-times-dev-template-1234567890.json (1.5KiB)..
100%|██████████████████████████████████████████████████████████| 1.58K/1.58K [00:00<00:00, 6.28KB/s]
Deploying API Gateway..
Scheduling..
Unscheduled bus-times-dev-zappa-keep-warm-handler.keep_warm_callback.
Scheduled bus-times-dev-zappa-keep-warm-handler.keep_warm_callback!
Your updated Zappa deployment is live!: https://xxxxxxxx.execute-api.eu-west-1.amazonaws.com/dev
```

Here is your app deployed now you can use the `https://xxxxxxxx.execute-api.eu-west-1.amazonaws.com/dev` link in the Alexa Skill setting

### Alexa Skill Setup
1. Go to the [Alexa Console](https://developer.amazon.com/edw/home.html) and click Add a New Skill.
2. Set "BusTimes" as the skill name and "bus times" as the invocation name, this is what is used to activate your skill. For example you would say: "Alexa, ask bus times what time come the two seven seven"
3. Select the `HTTPS` for the skill Endpoint and paste the https link from above. Click Next.
4. Copy the Intent Schema from the included IntentSchema.json.
5. Copy the Sample Utterances from the included SampleUtterances.txt. Click Next.
6. In order to test it, try to say some of the Sample Utterances from the Examples section below.
7. Your skill is now saved and once you are finished testing you can continue to publish your skill.
