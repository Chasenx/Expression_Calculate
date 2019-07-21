
log = print

def prefix_table(pattern):
    n = len(pattern)
    prefix = [0]
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length = length + 1
            prefix.append(length)
            i = i + 1
        else:
            if length > 0:
                length = prefix[length - 1]
            else:
                prefix.append(0)
                i = i + 1
    return prefix


def move_prefix_table(prefix):
    prefix.insert(0, -1)
    prefix.pop()
    return prefix


def kmp_search(text, pattern):
    # text[i],     len(text)    = m
    # pattern[j],  len(pattern) = n

    m = len(text)
    n = len(pattern)
    prefix = prefix_table(pattern)
    prefix = move_prefix_table(prefix)
    i = 0
    j = 0
    result = []
    
    while i < m:
        if (j == n - 1) and (pattern[j] == text[i]):
            result.append(i - j)
            j = prefix[j]

        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            j = prefix[j]
            if (j == -1):
                i = i + 1
                j = j + 1

    return result

if __name__ == "__main__":
    text = 'aabbaaa'
    pattern = 'aa'
    result = kmp_search(text, pattern)
    log(result)
