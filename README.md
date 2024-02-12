# Chino 🌸

<div>
  <p>
  Chino is a terminal-based chatbot. Powered by OpenAI. Uses RAG to generate
  </p>
  <a href="https://kuma.fosscu.org/status/LinkLiberate" target="_blank"><img src="https://badgen.net/badge/status/Under Development/red?icon=lgtm" alt=""></a>

  ![Version](https://img.shields.io/badge/Version-0.1.0-brightgreen.svg)
  ![Code Coverage](https://img.shields.io/codecov/c/github/SAMAD101/Chino)
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
  ![GitHub Issues](https://img.shields.io/github/issues/SAMAD101/Chino)
  ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/SAMAD101/Chino)
  ![Release Date](https://img.shields.io/github/release-date/SAMAD101/Chino)
  ![Commits](https://img.shields.io/github/commit-activity/m/SAMAD101/Chino)
  ![Last Commit](https://img.shields.io/github/last-commit/SAMAD101/Chino)
  ![Contributors](https://img.shields.io/github/contributors/SAMAD101/Chino)
  ![Repo Size](https://img.shields.io/github/repo-size/SAMAD101/Chino)
  ![Code Size](https://img.shields.io/github/languages/code-size/SAMAD101/Chino)
  ![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)

</div>

<p align="center">
  <img width="320" height="320" src="artwork/chino_logo_1.png" alt="Material Bread logo" style="margin-right:20px;">
</p>

<hr>

## 🐍 Python Version Support

This project is designed to be compatible with specific versions of Python for optimal performance and stability.

### Supported Python Version

- **Python 3.11.7**

> ❗️ For the best experience and performance, it is recommended to use the version mentioned above.

Before diving into the project, ensure that you have the correct Python version installed. To check the version of Python you currently have, execute the following command in your terminal:

```bash
python --version
```

### 🐍 Installing Python 3.11.7 with `pyenv`

**Protip:** Managing multiple Python versions is a breeze with [pyenv](https://github.com/pyenv/pyenv). It allows you to seamlessly switch between different Python versions without the need to reinstall them.

If you haven't installed `pyenv` yet, follow their [official guide](https://github.com/pyenv/pyenv) to set it up.

Once you have `pyenv` ready, install the recommended Python version by running:

```bash
pyenv install 3.11.7
```

> When you navigate to this project's directory in the future, `pyenv` will automatically select the recommended Python version, thanks to the `.python-version` file in the project root.

## Installation 🛠️

```bash
pip install chinoai
```


# 📦 Setup

## Local setup 🛠️ with Docker 🐳

> Coming soon!

<!--
- **Installing and running**:
  Before you begin, ensure you have docker installed. If not, refer to the [official documentation](https://docs.docker.com/engine/install/) to install docker.
  ```bash
  docker pull samad101/Chino
  docker run -d -p 8080:8080 --name pastepyprod samad101
  ```
  -->

<!--
- **Using docker-compose**:
  You can also use docker-compose to run the project locally by running the following command:
  <br>
  - **Clone the repository**:
  Get the project source code from GitHub:

  ```bash
  git clone https://github.com/SAMAD101/Chino.git
  ```

  - **Navigate to the Project Directory**:

  ```bash
  cd Chino
  ```

  - **Run the project using docker-compose**:

  ```bash
  docker-compose up
  ```
-->

## Local setup 🛠️ without Docker 🐳

### Setting Up the Project for development

- **Clone the Repository**:

  Get the project source code from GitHub:

  ```bash
  git clone https://github.com/SAMAD101/Chino.git
  ```

- **Navigate to the Project Directory**:

  ```bash
  cd Chino
  ```

- **Install the Project (from source)**:
-
  Use PDM to run the project:

  ```bash
  python3 -m pip install -e .
  ```

- **Run the project:**

  ```bash
  chino --help
  ```

## ⚠️ Note:

You will need an OpenAI API key to make it work. Get your API key from OpenAI website and set it as an environment variable:
```bash
export OPENAI_API_KEY="<your_api_key>"
```

## Usage 📖

Commands and options are available by running:

```bash
chino --help
```
For using the Retrieval Augmented Generation (RAG) features, follow these steps:

1. You will need to put your documents in the `~/.local/share/chino/data` directory in the root of the project.
    ```bash
    mkdir data
    ```
2. Create a directory in the root of the project called `~/.local/share/chino/chroma`.
    This directory will contain the OpenAI embeddings (embedding vectors) for the documents.

3. Process the documents and create the embeddings using the following command:
    ```bash
    chino migrate
    ```
> The directory data and chroma directories will be made more configurable in the future releases.
### Using Query mode:

Once your documents are processed. You can use the query mode to give prompts for the documents [RAG].
Start Chino by running:
```bash
chino start
```
and use `\q:` before your prompt to use it in query mode.
