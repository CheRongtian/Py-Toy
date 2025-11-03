# Note for git
- How to push my code to an existing repo (contains file already)
## First time:
```shell
cd /path/to/code
git init
git remote add origin https://github.com/xxxx/xxx.git
git pull origin main --rebase    # combine with current repo
git add .
git commit -m "what can I say"
git push origin main
```
## After that:
```shell
git push -u origin main
```
```-u``` equals to ```--set-upstream```, $means$ $set$ $default$
## Then:
```shell
git push
git pull
```

- Rather than:
```shell
git push origin main
git pull origin main
```
## Future:
name a file: ```gitpush.sh```
```shell
#!/bin/bash
msg=$1
if [ -z "$msg" ]; then
  msg="update"
fi
git add .
git commit -m "$msg"
git push origin main
```
-Then:
```shell
chmod +x gitpush.sh #provide permission
```

- In the future:
```shell
./gitpush.sh "what can I say"
```