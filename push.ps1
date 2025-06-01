param (
    [string]$commMess = "Default commit message"
)

pip freeze > requirements.txt
black .
git add .
git commit -m $commMess
git push