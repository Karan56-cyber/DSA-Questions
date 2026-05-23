def distinct_chars(s):

    hash_set=set()

    for ch in s:
        hash_set.add(ch)

    return len(hash_set)


s="programming"

print(distinct_chars(s))