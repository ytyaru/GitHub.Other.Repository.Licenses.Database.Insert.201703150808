#!python3
#encoding:utf-8
import os.path
import getpass
import Data
import command.repositories.Inserter
class Main:
    def __init__(self, user_name, path_db_account, path_db_other_repo, path_db_license):
        self.data = Data.Data(user_name, path_db_account, path_db_other_repo, path_db_license)
        self.inserter = command.repositories.Inserter.Inserter(self.data)
    def Run(self):
        print('GitHubリポジトリ情報を取得します。')
        url = 'start'
        while '' != url:
            print('GitHubリポジトリのURLを入力してください。(未入力+Enterで終了)')
            print('サブコマンド    l:既存リポジトリ')
            url = input()
            if '' == url:
                break
            elif 'l' == url or 'L' == url:
                self.inserter.Show()
            else:
                username = self.data.get_other_username(url)
                repo_name = self.data.get_other_repo_name(url)
                print("ユーザ名: " + username)
                print("リポジトリ名: " + repo_name)
                # 未登録ならDBへ挿入する（GitHubAPIでリポジトリ情報、言語情報、ライセンス情報を取得して）
                self.inserter.Insert(username, repo_name)


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

