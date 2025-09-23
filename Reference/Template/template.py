'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

'''
List all the parameters required by the task

You can use var_name convention for your variables
They will display automaticaly as "Var Name"
The allowed types are:
  'String', 'Boolean', 'Integer', 'Password', 'IpAddress',
  'IpMask', 'Ipv6Address', 'Composite', 'OBMFRef', 'Device'

 Add as many variables as needed
'''
dev_var = Variables()
dev_var.add('var_name', var_type='String')
dev_var.add('var_name2', var_type='Integer')

'''
context => Service Context variable per Service Instance
All the user-inputs of Tasks are automatically stored in context
Also, any new variables should be stored in context which are used across Service Instance
The variables stored in context can be used across all the Tasks and Processes of a particular Service
Update context array [add/update/delete variables] as per requirement

ENTER YOUR CODE HERE
'''
context = Variables.task_call(dev_var)
context['var_name2'] = int(context['var_name2']) + 1

'''
Format of the Task response :
JSON format : {"wo_status":"status","wo_comment":"comment","wo_newparams":{json_body}}
wo_status : ENDED [Green color] or FAILED [Red color] or WARNING [Orange color]
			-> While the Task is Running [means no response returned yet], task status is RUNNING [Blue color]
         -> When status is returned as FAILED, the Orchestration Engine stops the Process Execution from this Task
wo_comment : Appropriate Comment to display as per the success/failure of the Task
wo_newparams : json_body parameters returned from this Task

Functions task_success(), task_warning(), task_error(), task_pause() take care of creating a Json response from inputs
These function definitions can be found at : http://[YOUR_MSA_URL]/msa_sdk/msa_api.html
NOTE : For 'wo_newparams', always pass "context" [whether wo_status is ENDED/FAILED/WARNING to preserve it across Service Instance]
    -> The optional third argument mentions whether the json_response to be logged in the logfile : /opt/jboss/latest/logs/process.log
    -> If not passed, it's "true"
'''
MSA_API.task_success('Task OK', context)

