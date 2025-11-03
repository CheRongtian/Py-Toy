#!/bin/bash
msg=$1
if [ -z "$msg" ]; then
    msg="update"
fi
git add .
git commit -m "$msg"
git push origin main