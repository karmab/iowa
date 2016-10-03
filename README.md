- add debug parameter everywhere

- document cinder enabled backends

- add ldap support in keystone? keystone v3 ?

## CINDER
 - volume_driver can be either 
   - cinder.volume.drivers.lvm.LVMISCSIDriver . This is the default. In this case volume_group can be specified
   - cinder.volume.drivers.nfs.NfsDriver In this case , one can specify a different location and use the nfs_shares array to specify exports to add

