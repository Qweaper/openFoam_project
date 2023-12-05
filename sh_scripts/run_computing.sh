#!/bin/bash


source .env
blockMesh -case $ROOT_PATH/calculation/
# questions ?  $ROOT_PATH/calculation/transformPoints "scale=(0.04 0.02 0.01)"
pimpleFoam -case $ROOT_PATH/calculation/
paraFoam -case $ROOT_PATH/calculation/ &

