# このソフトウェアについて

他作GitHubリポジトリのライセンスを取得しDBへ挿入する。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite3](https://www.sqlite.org/index.html) 3.8.2

使用ライブラリは以下。感謝。

Library|License|Copyright
-------|-------|---------
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Requests License](http://docs.python-requests.org/en/master/user/intro/#requests-license), [Apache-2.0](http://opensource.org/licenses/Apache-2.0)|[Copyright 2017 Kenneth Reitz](http://docs.python-requests.org/en/master/user/intro/#requests-license)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## 必要なデータベースを作成する

* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)
    * [GiHubApi.Authorizations.Create](https://github.com/ytyaru/GiHubApi.Authorizations.Create.20170113141429500)
* [GitHub.Repository.Licenses.Database.Create.201703140912](https://github.com/ytyaru/GitHub.Repository.Licenses.Database.Create.201703140912)
	* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)	
* [GitHub.Licenses.Database.Create.201703140852](https://github.com/ytyaru/GitHub.Licenses.Database.Create.201703140852)
    * [GitHub.Licenses.Database.Insert.201703141133](https://github.com/ytyaru/GitHub.Licenses.Database.Insert.201703141133)
* [GitHub.Other.Repository.Database.Create.201703140946](https://github.com/ytyaru/GitHub.Other.Repository.Database.Create.201703140946)

## 設定

`Main.py`の以下コードで、GitHubユーザ名とDBパスを任意に設定する。

```python
if __name__ == "__main__":
    github_user_name = 'ytyaru'
    os_user_name = getpass.getuser()
    device_name = 'some_device'
    path_db_base = 'db/GitHub'
    path_db_account = '/media/{0}/{1}/{2}/GitHub.Accounts.sqlite3'.format(os_user_name, device_name, path_db_base)
    path_db_other_repo = './GitHub.Repositories.__other__.sqlite3'.format(os_user_name, device_name, path_db_base)
    path_db_license = './GitHub.Licenses.sqlite3'.format(os_user_name, device_name, path_db_base)
    main = Main(github_user_name, path_db_account, path_db_other_repo, path_db_license)
    main.Run()
```

# 実行

## 登録

```sh
python3 Main.py
```

```sh
GitHubリポジトリ情報を取得します。
GitHubリポジトリのURLを入力してください。(未入力+Enterで終了)
サブコマンド    l:既存リポジトリ
```

GitHubリポジトリURLを入力する。

```sh
https://github.com/google/google-api-python-client
```

URLからGitHubユーザ名とリポジトリ名を取得する。

```sh
ユーザ名: google
リポジトリ名: google-api-python-client
```

APIからリポジトリのライセンス情報、言語情報、リポジトリ情報を取得してDBへ挿入する。

## 表示

```sh
GitHubリポジトリのURLを入力してください。(未入力+Enterで終了)
サブコマンド    l:既存リポジトリ
```

上記で`l`を入力しEnterキー押下すると、DBのリポジトリ情報が表示される。

たとえば、以下のようなURLを入力した後で実行してみる。

```
https://github.com/kennethreitz/requests
https://github.com/requests/requests-oauthlib
https://github.com/pudo/dataset
https://github.com/newvem/pytz
https://github.com/gruns/furl
https://github.com/getanewsletter/BeautifulSoup4
https://github.com/martinblech/xmltodict
https://github.com/python-pillow/Pillow
https://github.com/ImageMagick/ImageMagick
https://github.com/google/google-api-python-client
```

以下、結果。

```
GitHubリポジトリのURLを入力してください。(未入力+Enterで終了)
サブコマンド    l:既存リポジトリ
l
Owner,RepoName,License
kennethreitz,requests,other
requests,requests-oauthlib,isc
pudo,dataset,mit
newvem,pytz,mit
gruns,furl,unlicense
getanewsletter,BeautifulSoup4,mit
martinblech,xmltodict,mit
python-pillow,Pillow,other
ImageMagick,ImageMagick,other
google,google-api-python-client,other
```

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
