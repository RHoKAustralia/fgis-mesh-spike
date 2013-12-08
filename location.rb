require 'bundler/setup'
require 'em-serialport'
require 'eventmachine'

if ARGV.length < 2
  puts "Usage: location.rb /dev/tty.usbserial-xxxx TruckId "
  exit 1
end
comdevice = ARGV.shift
truck_id = ARGV.shift

data = "{ \"truck_guid\" : \"#{truck_id}\", \"lat\" : \"-37.8209157\", \"lng\" : \"145.0385818\" }\n"

buffer = ""

EM.run do
  serial = EventMachine.open_serial(comdevice, 38400, 8, 1, 0)
  
  EventMachine.add_periodic_timer(15) {
    serial.send_data data
  }

  serial.on_data do |data|
    # do something with data
    buffer += data
    if buffer =~ /\n$/
      p buffer
      buffer=""
    elsif buffer =~ /\n.*$/
      lines = buffer.split("\n")
      buffer = lines.pop
      p lines.join("\n")
    end
  end
end