# Contribution Instructions

Thank you for your interest in contributing to Tweet Scheduler! This document outlines the process for contributing to the project.

## Getting Started

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Install the required dependencies 

4. Create a Twitter API key and access token by following these steps:

5. Create a Twitter developer account if you don't already have one.

6. Create a new app and generate your API key, API secret key, access token, and access token secret.

7. Add your API key, API secret key, access token, and access token secret to a `.env` file in the root directory of the project:

``` python
CONSUMER_KEY=<your_consumer_key>
CONSUMER_SECRET=<your_consumer_secret>
ACCESS_TOKEN=<your_access_token>
ACCESS_TOKEN_SECRET=<your_access_token_secret>
```

## Making Changes

1. Create a new branch for your changes:

``` git
git checkout -b feature/<feature-name>
```

2. Make your changes to the code.

3. Test your changes by running the program and ensuring that it works as expected.

4. Commit your changes:

``` git
git add .
git commit -m "Your commit message here"
```

5. Push your changes to your forked repository:

``` git
git push origin feature/<feature-name>
```

6. Create a pull request on GitHub from your forked repository to the original repository.

7. Wait for your pull request to be reviewed and merged.

## Code Style

Please adhere to the following code style guidelines when making changes to the code:

=> Use 4 spaces for indentation.

=> Use PEP 8 style guide for Python code.

=>Use clear and concise variable names.

=> Use comments to explain any complex or unclear code.

## Reporting Errors and Bugs

If you find a bug in the program, please create a new issue on GitHub with the following information:

    => A clear and descriptive title.
    => A detailed description of the bug, including any error messages or unexpected behavior.
    => Steps to reproduce the bug.
    => Any additional information that may be helpful in resolving the bug.
