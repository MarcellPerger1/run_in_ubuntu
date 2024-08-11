from pythonfuzz.fuzzer import Fuzzer


def fn(buf):
    if buf[0] == '\x00':
        return True
    elif buf[0] == '\x01':
        return 2
    elif buf[0] == '\x44':
        return 4
    else:
        return 77


if __name__ == '__main__':
    fn2 = Fuzzer(fn)
    fn2.start()
