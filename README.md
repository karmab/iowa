- document cinder enabled backends

- add ldap support in keystone? keystone v3 ?

- document how to run the role with a custom variables files ( and with a specific component through tags)

##KEYSTONE
 make sure /var/log/keystone/keystone.log belongs to keystone !!!!!
 seems two db_sync are needed for keystone ????


## CINDER
 - volume_driver can be either 
   - cinder.volume.drivers.lvm.LVMISCSIDriver . This is the default. In this case volume_group can be specified
   - cinder.volume.drivers.nfs.NfsDriver In this case , one can specify a different location and use the nfs_shares array to specify exports to add

## NEUTRON
 - grab tenant id and inject it in the conf
 - set tunneling ip stuff and create br-tun

## NOVA
 - documento nova.novncproxy_url as it cant be set in defaults var file


## RUN SPECIFIC COMPONENT

##OVERRIDE VARIABLES

´´´
ansible-playbook init.yml --extra-vars "@samples/madrid.yaml"
´´´

´´´
ansible-playbook init.yml --tags keystone
´´´

# DEPLOYING MULTIPLE NODES WITH ANSIBLE

- make the role visible
```
export ANSIBLE_ROLES_PATH=roles
```

- controller
```
ansible-playbook -i ~/CODE/git/KARIM/kcli/extra/klist.py samples/barcelona/controller.yml --extra-vars @samples/barcelona/variables.yml --tags common,controller
```

- compute
```
ansible-playbook -i ~/CODE/git/KARIM/kcli/extra/klist.py samples/barcelona/compute.yml --extra-vars @samples/barcelona/variables.yml --tags common,compute
```




