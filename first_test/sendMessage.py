import serial
import sys
import glob
import os


def main():
    send_message(b'message')
    while (input() != 'q'):
        send_message(b'message')


def active_ports_scan():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startwith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise OSError.EnvironmetError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            #print(s.get_settings())
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
            #print('Проблема с портом {0}'.format(port))
    return result


def send_message(message, repeat = 0):
    act_ports = active_ports_scan()
    print('Please, select port:')
    for port in range(0, len(act_ports)):
        print(str(port + 1) + '.', act_ports[port])
    selected_port = int(input('Choose: '))
    port_num = act_ports[selected_port - 1]
    port = serial.Serial(port_num)
    port.write(message)
    print('В порт отправлено:', message)


if __name__ == '__main__':
    main()
