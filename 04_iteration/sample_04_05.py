"""sample 04.05"""

count = 0
while True:
    count += 1

    if count % 2 == 0:
        continue

    if count >= 10:
        break

    print(count)
