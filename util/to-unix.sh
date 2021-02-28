#!/usr/bin/env bash

basedir=$(dirname "$0")

find $basedir/.. \( -path $basedir/../.git -o -path $basedir/../venv \) -prune -false -o -name "*.py" | xargs -I [] dos2unix []
find $basedir/../yalang -name "*.py" | xargs -I [] dos2unix []
find $basedir/../bin -name "*.py" | xargs -I [] dos2unix []
find $basedir/../test -name "*.py" | xargs -I [] dos2unix []
