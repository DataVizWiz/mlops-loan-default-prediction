param (
    [string]$commMess
)

pip freeze > requirements.txt
black .
git add .
git commit -m $commMess
git push