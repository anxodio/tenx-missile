import time
import usb.core
import usb.util


class MissileLauncher(object):
    _VENDOR_ID = 0x1130
    _PRODUCT_ID = 0x0202

    _CMD_FILL = [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    _STOP = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08]
    _LEFT = [0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08]
    _RIGHT = [0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x08]
    _UP = [0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x08, 0x08]
    _DOWN = [0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x08, 0x08]
    _UPLEFT = [0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x08, 0x08]
    _UPRIGHT = [0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x08, 0x08]
    _DOWNLEFT = [0x00, 0x01, 0x00, 0x00, 0x01, 0x00, 0x08, 0x08]
    _DOWNRIGHT = [0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x08, 0x08]
    _FIRE = [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x08]

    def __init__(self):
        self.connect()

    def connect(self):
        self._device = usb.core.find(
            idVendor=self._VENDOR_ID,
            idProduct=self._PRODUCT_ID)
        if self._device is None:
            raise ValueError("Missile Launcher not found. Is it connected?")

        def _get_interface(num):
            if self._device.is_kernel_driver_active(num):
                self._device.detach_kernel_driver(num)
            usb.util.claim_interface(self._device, num)
            usb.util.release_interface(self._device, num)

        _get_interface(0)
        _get_interface(1)
        self._device.set_configuration()

    def left(self, ms=500):
        self._send_timed_command(self._LEFT, ms)

    def right(self, ms=500):
        self._send_timed_command(self._RIGHT, ms)

    def up(self, ms=500):
        self._send_timed_command(self._UP, ms)

    def down(self, ms=500):
        self._send_timed_command(self._DOWN, ms)

    def upleft(self, ms=500):
        self._send_timed_command(self._UPLEFT, ms)

    def downleft(self, ms=500):
        self._send_timed_command(self._DOWNLEFT, ms)

    def upright(self, ms=500):
        self._send_timed_command(self._UPRIGHT, ms)

    def downright(self, ms=500):
        self._send_timed_command(self._DOWNRIGHT, ms)

    def fire(self):
        self._send_command(self._FIRE)

    def stop(self):
        self._send_command(self._STOP)

    def _send_timed_command(self, command, ms):
        self._send_command(command)
        if ms:
            time.sleep(ms / 1000)
            self.stop()

    def _send_command(self, command):
        self._send_headers()
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x00, command+self._CMD_FILL)

    def _send_headers(self):
        # ord('U'), ord('S'), ord('B'), ord('C') => 85, 83, 66, 67
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x01, [85, 83, 66, 67, 0, 0, 4, 0])
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x01, [85, 83, 66, 67, 0, 64, 2, 0])
