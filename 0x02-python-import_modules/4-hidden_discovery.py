#!/usr/bin/python3
if __name__ == "__name__":
    import hidden_4

    for item in dir(hidden_4):
        if item.startswith('__'):
            continue
        print(item)
