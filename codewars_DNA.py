def likes(names):
    if not names:
        return 'no one likes this'
    if len(names) == 1:
        return '{} likes this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0], names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    if len(names) > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)


if __name__ == '__main__':
    print(likes(['Peter', 'Bob', 'fas', 'eee']))
