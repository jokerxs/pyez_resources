pyez_resources
==============
A resource module for [py-junos-eznc](https://github.com/Juniper/py-junos-eznc) for handling **prefix-list** entries.

Py-JunOS-eznc is the long-waited tool to aid automated remote management of JunOS devices.
**pyez_resources** is extending **py-junos-eznc** with prefix list manipulation resource object.

I wrote this module to automate configuration of JunOS firewall through prefix-list.
Consider this firewall term configuration:
```
term drop-src {
    from {
        source-prefix-list {
            drop-src;
        }
    }
    then {
        discard;
    }
}
```
And here is the matching prefix list:
```
prefix-list drop-src {
    10.1.1.10/32;
    192.168.1.0/24;
}
```

Now with py-junos-eznc I can add and remove entries from prefix list and thus control what JunOS divice is blocking.

== Install ==
Copy **prefix_*.py** to /usr/local/lib/python2.7/dist-packages/jnpr/junos/cfg/

== Usage ==
An example script:
```py
#!/usr/bin/env python
#

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.cfg.prefix_list import PrefixList

plist = {}
lists = [ 'drop-src', 'drop-dst' ]
action = 'list'
jdev = 'juniper2'
juser = 'netop'
juser_keyfile = '/root/.ssh/netop.id_rsa'


# connect to JunOS device
dev = Device(host=jdev, user=juser, port=22, ssh_private_key_file=juser_keyfile)
try:
    dev.open()
except:
    exit('ERROR: cannot connect to JunOS device wuth: host= %s, user=%s' % (jdev, juser))

# create a prefix-list object
pl = PrefixList(dev)

for plist_name in lists:
    print("\n%s:" % plist_name)
    for item in pl[plist_name].prefix_list_item.list:
        print("  %s" % item)

dev.close()
```
