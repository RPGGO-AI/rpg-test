SHELL := /bin/bash
#user_name := $(shell git config user.name)
user_name := $(shell whoami)

PY3  := python3
VENV := .venv
BIN  := $(VENV)/bin
MAKEFILE_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))

APP        := rpg-test
ENV 	   ?= test

.PHONY: init
init:
	$(PY3) -m venv $(VENV)
	$(BIN)/python3 -m pip install --upgrade pip
	$(BIN)/pip3 install wheel
	$(BIN)/pip3 install -r requirements.txt
	echo "export PYTHONPATH=\$$PYTHONPATH:$(MAKEFILE_DIR)" >> ~/.bashrc

.PHONY: install
install:
	$(BIN)/pip3 install -r requirements.txt

.PHONY: deploy
deploy:
	export PYTHONPATH=$$PYTHONPATH:$(MAKEFILE_DIR) && $(BIN)/python3 online_log/app.py