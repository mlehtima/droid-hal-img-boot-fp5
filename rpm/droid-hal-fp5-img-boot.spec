%define device fp5

%define mkbootimg_cmd mkbootimg --cmdline 'androidboot.selinux=permissive audit=0' --header_version 3 --os_version 14.0.0 --os_patch_level 2024-10 --kernel %{kernel} --ramdisk %{initrd} --output

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/panel0-backlight/brightness
%define display_brightness 1024

%define lvm_root_size 10000

%include initrd/droid-hal-device-img-boot.inc
