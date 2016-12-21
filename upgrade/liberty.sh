ansible-playbook -i ~/klist.py subscriptions_liberty.yml
ansible-playbook -i ~/klist.py site.yml -vvv --tags controller,mongodb,mysql,rabbitmq,api
ansible-playbook -i ~/klist.py compute.yml --tags compute
