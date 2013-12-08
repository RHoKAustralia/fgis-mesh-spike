from synapse.switchboard import *

@setHook(HOOK_STARTUP)
def startupEvent():
    initUart(1, 38400) # <= put your desired baudrate here!
    flowControl(1, False) # <= set flow control to True or False as needed
    crossConnect(DS_UART1, DS_STDIO)
    

@setHook(HOOK_STDIN)
def process():
    print "HELLO"