import datetime

# 1 task
today = datetime.date.today()
subtract_5 = today - datetime.timedelta(days = 5)
print(f"today: {today}\n5 days ago: {subtract_5}")


# 2 task 
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)


# 3 task
print(datetime.datetime.today())
print(datetime.datetime.today().replace(microsecond = 0))


# 4 task
f = list(map(int, input("Frirst date: ").split()))
s = list(map(int, input("Second date: ").split()))

a = datetime.date(f[0], f[1], f[2]) - datetime.date(s[0], s[1], s[2])
print (a.total_seconds())