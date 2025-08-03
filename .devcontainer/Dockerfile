FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/home/vscode/.local/bin:$PATH"

WORKDIR /workspace

USER root

