import liblo, sys
import grovepi

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4
grovepi.pinMode(relay,"OUTPUT")

try:
    server = liblo.Server(5005)
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
        if a == 3:
            # switch on for 5 seconds
            grovepi.digitalWrite(relay,1)
            print ("on")
            time.sleep(5)

            # switch off for 5 seconds
            grovepi.digitalWrite(relay,0)
            print ("off")
            time.sleep(5)

server.add_method("/foo/bar", 'if', foo_bar_callback)
server.add_method(None, None, fallback)

# loop and dispatch messages every 100ms
while True:
    try:
        server.recv(100)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
