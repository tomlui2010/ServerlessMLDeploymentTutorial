# ServerlessMLDeploymentTutorial
Deploy machine learning models using serverless templates on AWS Lambda.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

Use pre-trained model ResNet50 and predict the animal in the image provided. 
Uses AWS SAM to setup a lambda function and an API gateway infrastructure. 
The lambda installs the pre-trained model and using this model provides the Top 3 predictions of the animal in the picture provided. 
Pre-trained model is build with 'keras' library. 
Used AWS lambda python base image for docker 

## Table of Contents

1. [Installation](#installation)
2. [References](#references)

## Installation

To install and set up the project, follow these steps:
```

    1. Clone the repository to your local machine:
        [!Git Repo](git clone https://github.com/tomlui2010/ServerlessMLDeploymentTutorial.git)

    2. Navigate to the project directory:
        cd serverless-ml-deployment

    3. Create a Python virtual environment:
        # For Unix/macOS
        python3 -m venv ~/.venv

    4. Activate the virtual environment:
        source venv/bin/activate

    5. Install AWS SAM
        pip install aws-sam-cli

    6. Build using SAM
        sam build

    Note: SAM template is called template.yaml. This will create the require lambda function, its api gateway and IAM role

    7. Run your AWS Lambda functions locally and test through a local HTTP server host
        sam local start-api

    Note: Postman collection is added to the project under ~/serverless-ml-deployment/postman

    8. Deploy 
    sam deploy --guided
```
Note: Remember to deactivate the virtual environment when you're done working on the projec.

API endpoint: (implicitly created API out of Events key under Serverless::Function)
```
    "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/whatsinmyimage/"
    Route: /predict
```

## References

- https://aws.amazon.com/blogs/compute/deploying-machine-learning-models-with-serverless-templates/
- https://aws.amazon.com/blogs/compute/creating-faster-aws-lambda-functions-with-avx2/
- https://docs.aws.amazon.com/serverless-application-model/

