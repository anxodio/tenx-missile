Tenx USB Missile Launcher Python Driver
=======================================

This is a Python driver to control the Tenx USB Missile Launcher (`0x1130`/`0x0202`).

It is tested in Python3 and an Ubuntu based distro.

Executing as non root
---------------------

In order to connect to the USB without being a super user, you need to add an udev rule.

As a super user, just create a new file `/etc/udev/rules.d/99-missile.rules` with the following content:
```
SUBSYSTEM=="usb", ATTR{idVendor}=="1130", ATTR{idProduct}=="0202", MODE="666"
```
Then, restart udev with:
```bash
# udevadm trigger
```

Acknowledgements
----------------
- https://www.npmjs.com/package/tenx-usb-missile-launcher-driver
- https://github.com/AlexNisnevich/sentinel
- https://github.com/pddring/usb-missile-launcher
