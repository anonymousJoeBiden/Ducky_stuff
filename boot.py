import usb_hid
import usb_cdc

usb_cdc.enable(console=False, data=False)

usb_hid.enable((usb_hid.Device.KEYBOARD,usb_hid.Device.CONSUMER_CONTROL,))