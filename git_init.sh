#!/bin/bash

echo Input project name:
read PROJECT_NAME

mkdir $PROJECT_NAME

PWD=`pwd`
touch $PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace

echo '{' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo '	"folders": [' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo '		{' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo '			"path": "."' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo ' 		}' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo '	]' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace
echo '}' >>$PWD/$PROJECT_NAME/$PROJECT_NAME-workspace.code-workspace

touch $PWD/$PROJECT_NAME/.gitignore

echo '*.code-workspace' >>$PWD/$PROJECT_NAME/.gitignore
echo '*.db' >>$PWD/$PROJECT_NAME/.gitignore
echo '*.log' >>$PWD/$PROJECT_NAME/.gitignore
echo '/__pycache__/*' >>$PWD/$PROJECT_NAME/.gitignore

git init $PWD/$PROJECT_NAME
git -C $PWD/$PROJECT_NAME branch -m master main 

PROJECT_SSH=$(python3 ~/bash/git_init/github_generate_repository.py $PROJECT_NAME)

git -C $PWD/$PROJECT_NAME remote add origin $PROJECT_SSH