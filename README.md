# Scenario and Review Criretia

You will be required to provide screenshots of the services created, the output of the web application, the URL of your deployment and the Github URL where you have your code to showcase the completion of the project. Ensure that the screenshots are clear and URLs are accessible. Ensure that no sensitive information is exposed through your Github repository.

1. Use Watson APIs to create Language Translator Service. 1pt
2. Create an instance of the Language Translator Service in your Python code. 1pt
3. Create a function that translates English to French. 2pt
4. Create a function that translates French to English. 2pt
5. Write unit tests to test the englishToFrench function with assertEqual and assertNotEqual 2pt
6. Write unit tests to test the frenchToEnglish function with assertEqual and assertNotEqual 2pt
7. Run coding standards check against the functions above. 3pt
8. Run unit tests and interpret the results. 4pt
9. Package the above functions and tests as a standard python package. 2pt
10. Import the package in the server code and provide translation endpoints. 4pt
11. Check English to French translation 1pt
12. Check French to English translation 1pt

You will be required to take screenshots as you complete the assignment and upload them for your peers to review. You will be awarded points up to the maximum given for the successful submission of the screenshots showing your work. Points will be awarded for the completeness of the work.

# Project Overview

This project has several steps that you must complete. The high-level step list given below will help to provide you with an overview of the whole project. The project is divided into smaller labs with detailed instructions for each step. You must complete all labs to complete the project successfully. Project Breakdown

## Prework: Sign up for IBM Cloud Lite account and create a Watson Language Translator service.

1. Create an IBM Cloud Lite account, if you don't have one already.
2. Create an instance of the Watson Language Translator.

## Create Python Server side

1. Fork and clone the skeleton project on your GitHub.
2. Create an instance of the Watson Language Translator in the translator.py
3. Create two functions, one to translate from English to French and the othet to translate from French to English in translator.py
4. Write unit tests to test the two functions
5. Run coding standards check against the two functions
6. Run unit tests and ensure the tests pass.
7. Package the above functions and tests as a standard python package
8. Import the package in server.py. Create two end points in server.py /englishToFrench and /frenchToEnglish and test them on local server.
9. Deploy the application on IBM Cloud.

### Deploy the server application

```
- Deploy the server application so that it is accessible through browser
```

## Submit your project for grading

You will need to submit the URL of your server application that you have deployed, screenshots of the translation and the link to your github repository.
