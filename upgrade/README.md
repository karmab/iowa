to deploy,
you can use the provided kcli plan, so run 

`kcli plan nework`

then launch the ansible playbooks

`ansible-playbook -i ~/klist.py site.yml -vvv --tags controller,mongodb,mysql,rabbitmq,api`

`ansible-playbook -i ~/klist.py compute.yml --tags compute`

to upgrade,
set common.version accordingly (typically in a group_vars file)
launch liberty.sh that will do the following:

- update the repos 
- update all the nodes except compute
- update compute nodes

Note that you could alternatively run a full yum update task after updating the repos
