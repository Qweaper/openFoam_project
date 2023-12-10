#!/bin/bash


source .env
X=$( bc -l <<< "$1 * 0.01" )
Y=$( bc -l <<< "$2 * 0.01" )
blockMesh -case $ROOT_PATH/calculation/
transformPoints "scale=(0${X} 0${Y} 0.01)" -case $ROOT_PATH/calculation/
pimpleFoam -case $ROOT_PATH/calculation/
paraFoam -case $ROOT_PATH/calculation/ 
