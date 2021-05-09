import serial
import sys
import glob
import Actions


def quit(*args):
    exit()


def gui_mode(*args):
    if len(args) > 0:
        print('GUI Mode with *args')
    else:
        print('GUI Mode')


def active_ports_scan():
    if sys.platform.startswith('win'):
        #ports = ['COM%s' % (i + 1) for i in range(256)] -- это называется "генератор списка"
        ports = []
        for i in range(256):
            ports.append('COM' + str(i + 1))
    elif sys.platform.startswith('linux') or sys.platform.startwith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def listen_port(*args):
    port_name = ''.join(args)
    print('Слушаю порт {0}:'.format(port_name))
    try:
        while True:
            port = serial.Serial(port_name, 9600)
            port.timeout = 3
            message = port.readline(10)
            if message == b'pon\r\n':
                print('Включаю')
                port.close()
            elif message == b'pof\r\n':
                port.close()
                print('Выключаю контроллер видеостены')
                Actions.shutdown()
                break
            elif message == b'rst\r\n':
                port.close()
                print('Перезагружаю контроллер видеостены')
                Actions.shutdown()
                break
            elif message == b'vup\r\n':
                print('Громкость +')
                Actions.volume_up()
                port.close()
            elif message == b'vdn\r\n':
                print('Громкость -')
                Actions.volume_down()
                port.close()
            elif message == b'mut\r\n':
                print('Тишина')
                Actions.volume_mute()
                port.close()
            elif message == b'ps1\r\n':
                print('Preset 1')
                Actions.start_preset('1.txt')
                port.close()
            elif message == b'ps2\r\n':
                print('Preset 2')
                Actions.start_preset('2.txt')
                port.close()
            elif message == b'ps1\r\n':
                print('Preset 3')
                Actions.start_preset('3.txt')
                port.close()
            else:
                print('Я принял неизвестное сообщение :(')
                print('Вот оно: {0}'.format(message))
                port.close()
    except:
        print('Возникло исключение!')
        quit()
    finally:
        port.close()


func_dict = {'quit': quit,
             'gui_mode': gui_mode,
             'listen_port': listen_port}
