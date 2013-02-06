import contextlib


@contextlib.contextmanager
def opened(filename, mode="r"):
    f = open(filename, mode)
    try:
        print "before yeild"
        yield f
        print "after yeild"
    finally:
        f.close()


with opened("/etc/passwd") as f:
    for line in f:
        print line.rstrip()
