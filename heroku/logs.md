# logs

## log source
```
--source app
--source heroku
--source app --dyno api
```

## log history
> see last 200 logs (max=1500)(n=num)
```
heroku logs -n 200
```

## real-time tail
> live stream of logs
```
heroku logs --tail
heroku logs -t
```