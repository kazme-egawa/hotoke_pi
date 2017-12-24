import liblo, sys
try:
    server = liblo.Server(8000)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

def foo_bar_callback(path, args):
    i, f = args
    print "received message '%s' with arguments '%d' and '%f'" % (path, i, f)

def fallback(path, args, types, src):
    print "got unknown message '%s' from '%s'" % (path, src.get_url())
    for a, t in zip(args, types):
        print "argument of type '%s': %s" % (t, a)

server.add_method("/foo/bar", 'if', foo_bar_callback)
server.add_method(None, None, fallback)

# loop and dispatch messages every 100ms
while True:
    server.recv(100)
