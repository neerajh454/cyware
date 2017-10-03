# cyware

I have created api to search the users from github api and here is the endpoint for url.

/search-user/?name=neeraj


parameters can be passed.

1 - gt_created - date in 2013-05-15 format. It will give users whose repository is created on or after given date.
2 - gt_created - date in 2013-05-15 format. It will give users whose repository is created on or before given date.
3 - gt_repos - gives users whose repos is greater than given value.
4 - lt_repos - gives users whose repos is less than given value
5 - gt_followers - gives users whose followers more than given value.
6 - lt_followers - gives users whose followers less than given value.
7 - location - location of user
8 - language - language for user


I have created cron job for update users and number of api hits, so please run following command.

python manage.py crontab add


