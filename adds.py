from tasks import add
aa = add.delay(4, 4)

print(add.apply_async((2, 3)))

print(aa.get(timeout=1))