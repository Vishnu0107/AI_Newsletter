#!/bin/bash

# Variables
model_name = "llama2"
custom_model_name = "local_llama"

ollama pull $model_name

ollama create $custom_model_name -f ./Llama2Modelfile