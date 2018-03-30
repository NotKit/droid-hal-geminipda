# These and other macros are documented in dhd/droid-hal-device.inc
%define device geminipda
%define vendor planet

%define vendor_pretty Planet
%define device_pretty Gemini PDA

%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/bugreports\
/d\
/enableswap.sh\
/file_contexts.bin\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
/verity_key\
%{nil}

%define makefstab_skip_entries /system

%include rpm/dhd/droid-hal-device.inc
