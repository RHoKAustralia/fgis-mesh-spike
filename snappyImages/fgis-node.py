from synapse.switchboard import *

broadcastCounter = 0

@setHook(HOOK_STARTUP)
def startupEvent():
    initUart(1, 38400) # <= put your desired baudrate here!
    flowControl(1, False) # <= set flow control to True or False as needed
    crossConnect(DS_UART1, DS_STDIO)
    

@setHook(HOOK_STDIN)
def process(line):
    #cmd, data =  line.split(',')
    #if cmd =="rand
    print line
        
def dataCallback(result):
    print 'Received Data: ', result

@setHook(HOOK_1S)   
def networkBroadcast():
    global broadcastCounter
    if(broadcastCounter >= 10):
        broadcastCounter=0
        #mcastRpc(1, 3, 'dataCallback', 'hello')
        rpc('\x5E\x31\xEB', 'dataCallback', broadcastCounter)
    else:
        broadcastCounter = broadcastCounter + 1
    