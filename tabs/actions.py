

'''
This function handles the action performed when the start/run
button for an individual task in the task tab is pressed.
'''
def task_tab_action_start(task_data: dict):
    print(f"Task Tab , Task ID {task_data['ID']} Started")

'''
This function manages the action  taken  when  the  terminate 
button for an individual task in the task tab is pressed.
'''
def task_tab_action_terminate(task_data: dict):
    print(f"Task Tab , Task ID {task_data['ID']} Terminated")

'''
This  function  is  responsible  for  handling   the   action 
triggered when the edit button for an individual task in  the 
task   tab   is   pressed.   Simply   update   the  value  of 
'column_data[each_key]['label']['text']' to display it in the 
interface.
'''
def task_tab_action_edit(task_data: dict, column_data: dict):
    print(f"Task Tab , Task ID {task_data['ID']} Edit")
    for each_key in list(column_data.keys())[1:-1]:
        column_data[each_key]["label"]["text"] = each_key + "777"
    print(f"Task Tab , Task ID {task_data['ID']} Edited")

'''
This function oversees the action executed  when  the  delete 
button for an individual task in the task tab is pressed.
'''
def task_tab_action_delete(task_data: dict):
    print(f"Task Tab , Task ID {task_data['ID']} Deleted")


'''
This function oversees the action executed  when  the  delete 
button for an individual biller in the billing tab is pressed.
'''
def billing_tab_action_delete(task_data: dict):
    print(f"Billing Tab , Billing ID {task_data['ID']} Deleted")

'''
This  function  is  responsible  for  handling   the   action 
triggered when the edit button for an individual biller in the 
billing   tab   is   pressed.  Simply   update  the  value of 
'column_data[each_key]['label']['text']' to display it in the 
interface.
'''
def billing_tab_action_edit(task_data: dict,column_data:dict):
    print(f"Billing Tab , Task ID {task_data['ID']} Edit")
    for each_key in list(column_data.keys())[1:-1]:
        column_data[each_key]["label"]["text"] = each_key+"555"
    print(f"Billing Tab , Task ID {task_data['ID']} Edited")

