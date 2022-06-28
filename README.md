## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

Creating conda environment
```
conda create -p venv python==3.7 -y
```
conda activate venv
```
OR
```
conda activate venv/
```
pip install -r requirements.txt
```
to add all file from current directory
```
git add .
```
to add particular file
```
git add <filename1> <filename2>
```
>Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To check remote url
```
git remote -v
```
To push commited version
```
git push origin main
```
To setup CI/CD pipline in heroku we need below 3 information

1. HEROKU_EMAIL = bansipatel6899.bp@gmail.com
2. HEROKU_API_KEY = <API Key>
3. HEROKU_APP_NAME = ml-regression-project1


Build Docker Image
```
docker build -t <image_name>:<tag_name> .
```
>Note Image name for docker must be in lowercase

```
To list docker images
```
docker images
```
To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image ID>
```
To check running cotainer in docker
```
docker ps
```
To stop docker image
```
docker stop <container id>
```
To install all required libraries install automatically
```
python setup.py install
```
