def hundred_number():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_number()

print(sum(g))

print(next(g))
print(next(g))

print(sum(g))
