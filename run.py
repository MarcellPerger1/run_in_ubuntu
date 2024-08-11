from pythonfuzz.fuzzer import Fuzzer


def fn(buf):
    if buf[0] == '\x00':
        return True
    elif buf[0] == '\x01':
        return 2
    elif buf[0] == '\x44':
        return 4
    elif buf[0] == '\x02':
        return 2
    elif buf[0] == '\x03':
        return 4
    elif buf[0] == '\x04':
        return 2
    elif buf[0] == '\x45':
        return 4
    elif buf[0] == '\x06':
        return 2
    elif buf[0] == '\x47':
        return 4
    elif buf[0] == '\x08':
        return 2
    elif buf[0] == '\x49':
        return 4
    elif buf[0] == '\x12':
        return 2
    elif buf[0] == '\x13':
        return 4
    elif buf[0] == '\x14':
        return 2
    elif buf[0] == '\x15':
        return 4
    elif buf[0] == '\x16':
        return 2
    elif buf[0] == '\x17':
        return 4
    elif buf[0] == '\x18':
        return 2
    elif buf[0] == '\x19':
        return 4
    elif buf[0] == '\x20':
        return 2
    elif buf[0] == '\x21':
        return 4
    elif buf[0] == '\x22':
        return 2
    elif buf[0] == '\x23':
        return 4
    elif buf[0] == '\x24':
        return 2
    elif buf[0] == '\x25':
        return 4
    elif buf[0] == '\x26':
        return 2
    elif buf[0] == '\x27':
        return 4
    elif buf[0] == '\x28':
        return 2
    elif buf[0] == '\x29':
        return 4
    elif buf[0] == '\x30':
        return 2
    elif buf[0] == '\x31':
        return 4
    elif buf[0] == '\x32':
        return 2
    elif buf[0] == '\x33':
        return 4
    elif buf[0] == '\x34':
        return 2
    elif buf[0] == '\x35':
        return 4
    elif buf[0] == '\x36':
        return 2
    elif buf[0] == '\x37':
        return 4
    elif buf[0] == '\x38':
        return 2
    elif buf[0] == '\x39':
        return 4
    else:
        return 77


if __name__ == '__main__':
    fn2 = Fuzzer(fn)
    fn2.start()
