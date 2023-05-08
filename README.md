# Learn Basics of Github Actions

## What is Github Actions?
Github Actions is a CI/CD tool that is built into Github. It allows you to automate your workflow by creating workflows that are triggered by events.


## How to create a workflow?

1. Create a `.github` folder in the root of your repository.
2. Create a `workflows` folder inside the `.github` folder.
3. Create a `yaml` file inside the `workflows` folder.
4. Add the following code to the `yaml` file.

```yaml
name: Name of your workflow
on: # Events that trigger the workflow
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
jobs: # Jobs that run in the workflow

```

## What are jobs?
For showing the working of jobs, I have created a simple workflow that runs a job that prints a message.
