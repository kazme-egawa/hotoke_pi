import liblo, sys
try:
    target = liblo.Address("localhost",5005)
except liblo.AddressError, err:
    print str(err)
    sys.exit()
liblo.send(target, "/foo/bar", 1, "test")
