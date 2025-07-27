from user import User
from admin import Admin

me = User("kazuma", "aoyama", 511)
you = User("hiroto", "ono", 612)

me.greet_user()
me.describe_user()
you.greet_user()
you.describe_user()

me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attemts)
me.reset_login_attempts()
print(me.login_attemts)

adm = Admin("haruto", "mitani", 0, "投稿を追加する")
adm.show_previleges()

adm1 = Admin("sota", "fukumaru", -1, "投稿を追加する", "ユーザーを利用禁止にする")
adm1.show_previleges()