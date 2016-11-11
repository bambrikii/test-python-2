def most_significant(val):
    while val >= 10:
        val //= 10
    return val


print most_significant(123)
print most_significant(9876543210)
print most_significant(5)
print most_significant(-954)

print hash("123")
