#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

DOCUMENTATION = '''
module: subscription_repos
short_description: Handles repositories for rhel machines
description:
    - Longer description of the module
    - You might include instructions
version_added: "0.1"
author: "Karim Boumedhel, @karmab"
notes:
    - Details at https://github.com/karmab/iowa
requirements:
    - subscription manager and a rhel machine'''

EXAMPLES = '''
- name: Assign Openstack Liberty Repositories
  subscription_repos:
   repos:
     - rhel-7-server-rpms
     - rhel-7-server-rh-common-rpms
     - rhel-7-server-openstack-8-rpms
     - rhel-ha-for-rhel-7-server-rpms
     - rhel-7-server-extras-rpms
'''


def main():
    argument_spec = {
        "repos": {"required": True, "type": "list"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
        "only": {"default": 'no', "required": False, "type": "str", "choices": ['yes', 'no']},

    }
    module = AnsibleModule(argument_spec=argument_spec)
    repos = module.params['repos']
    state = module.params['state']
    only = module.params['only']
    if state == 'present':
        if only == 'yes':
            os.system("subscription-manager repos --disable='*'" % repos)
        repos = ' '.join(['--enable=' + repo for repo in repos])
        # result = os.system("subscription-manager repos %s" % repos)
        result = os.popen("subscription-manager repos %s" % repos).read()
        if 'Error' in result:
            module.fail_json(msg=result)
        meta = {'result': result}
        changed = True
        skipped = False
    else:
        repos = ' '.join(['--disable=' + repo for repo in repos])
        result = os.popen("subscription-manager repos %s" % repos).read()
        if 'Error' in result:
            module.fail_json(msg=result)
        meta = {'result': result}
        changed = True
        skipped = False
    module.exit_json(changed=changed, skipped=skipped, meta=meta)

if __name__ == '__main__':
    main()
