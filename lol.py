import os

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system(f'git commit --allow-empty -m "Commit {i} of {ip}"')	

print(f"Commited {ip} times")

if autoPush == "y":
	os.system('git push')
	
# git commit --allow-empty -m "New Commit at: $(date)"