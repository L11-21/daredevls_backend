#!/bin/bash
gcc -shared -o utils/viable.so -fPIC utils/viable.c
pip install -r requirements.txt
