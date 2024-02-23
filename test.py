def say_hello_bye(n):
    if n == 1:
        print(n, "Hello")
        print(n, "Bye!")
        return

    print(n, "Hello")
    say_hello_bye(n - 1)
    print(n, "Bye!")

n = int(input())
say_hello_bye(n)