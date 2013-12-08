# Fire Ground Information System - Mesh Networking Spike

The following repo is the result of the mesh networking spike done at the latest RHoK (Dec 2013).

The following capabilities were explored:
  - Enable broadcasting of location
  - Interact with the mesh networking hardware using serial.
  
## Prerequisites
  - 2 (or more) Synapse RF266PC1 https://www.sparkfun.com/products/11279
  - A [XBee Explorer USB](https://www.sparkfun.com/products/8687) or [XBee Explorer Dongle](https://www.sparkfun.com/products/9819) for each of the above
  - A copy of Portal to load the SnapPy images onto the device
  
## Replicating the Spike
The Synapse devices run an embedded version of python. The capabilities described above require uploading this 'snappy' script to each of the devices.
  
Firstly follow the spark fun tutorial at [https://www.sparkfun.com/tutorials/367](https://www.sparkfun.com/tutorials/367). This will introduce you to Portal and show you how to erase the existing SnapPy image. (Hint: I have found the inserting the radio at the right moment to be more reliable than trying to find and short GND and RST)

It is fine to have both of the devices plugged into the same computer.

Use portal to upload the SnapPy image in this repo to each of the devices. You will need to set the working directory to the root of this repo before you can find the snappy script in the available list. Keep in mind that once you program both of them you will lose the ability to communicate with them using portal.

Use the ruby script to connect to each of the USB serial devices and start broadcasting the location.

For example:
```
ruby location.rb /dev/tty.usbserial-AD02AICC TruckA
```

You should see the messages from the other truck come through over the wire.

Congratulations you can now broadcast the location of your truck to the entire mesh network.
