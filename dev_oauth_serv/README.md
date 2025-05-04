# OAuth 2.0 Provider:

Downloaded from `https://github.com/authlib/example-oauth2-server`

For more details follow author's page. This code is attached to current repository only for dev / testing purposes. In any environment different to dev it should be replaced with regular OAuth service


## How to run

Set Flask and Authlib environment variables:

```bash
# disable check https (DO NOT SET THIS IN PRODUCTION)
$ export AUTHLIB_INSECURE_TRANSPORT=1
```

Create Database and run the development server:

```bash
$ flask run
```

Now, you can open your browser with `http://127.0.0.1:5000/`, login with any
name you want, for TankBattleGame let's use `test_user`

Before testing, we need to create a client with `http://127.0.0.1:5000/create_client` and below values (for localhost):
* Client Name - `TankBattleGameApi`
* Client URI - `http://127.0.0.1:8000`
* Allowed Scope - `profile`
* Redirect URIs - `http://127.0.0.1:8000`
* Allowed Grant Types - `authorization_code`, `password`
* Allowed Response Types - `code`
* Token Endpoint Auth Method - `client_secret_basic`

### Generate token:

Get code by opening below link in browser, with client_id generated in previous step.
```
http://127.0.0.1:5000/oauth/authorize?response_type=code&client_id=${client_id}&scope=profile
```
Consent and submit, ext you should be redirected to `${redirect_uri}/?code=${code}`, in current example it will be `http://127.0.0.1:8000/?code=${code}`. Copy code form url.

Now generate token with:

```bash
$ curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=authorization_code -F scope=profile -F code=${code}
```

With retrieved tokken access endopoint `/api/me`:

```bash
$ curl -H "Authorization: Bearer ${access_token}" http://127.0.0.1:5000/api/me
```