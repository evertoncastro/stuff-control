#!/usr/bin/env bash

export NVM_DIR=$HOME/.nvm;
source $NVM_DIR/nvm.sh;

nvm use 16

cd frontend
rm -rf build
yarn build

mkdir -p build/root/
for file in $(ls build | grep -E -v '^(index\.html|static|root)$'); do
    mv "build/$file" build/root;
done

cd ..

poetry env use python3.11
rm -rf application/static/
python manage.py collectstatic --no-input

