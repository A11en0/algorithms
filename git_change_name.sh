
git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_NAME" = "xiulinhfut" ]; then \
    export GIT_AUTHOR_NAME="a11en" GIT_AUTHOR_EMAIL="g352415441@mail.com"; \
fi
'
