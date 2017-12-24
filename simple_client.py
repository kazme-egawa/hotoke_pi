import liblo, sys
try:
    target = liblo.Address("127.0.0.1",8000)
except liblo.AddressError, err:
    print str(err)
    sys.exit()
liblo.send(target, "/foo/message1", 123, 456.789, "test")
