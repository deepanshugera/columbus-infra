import pandas as pd
import json
import gc
def execute_command(df, command):
	#locals()={}
	result=""
	try:
		e_command = "commad_output="+command
		exec(e_command)
		result=locals()['commad_output']
	except:
		result="Could not execute command. Recheck whether your syntax is correct"
	print("command : " + e_command)
	#result= locals()
	result=str(result)
	if "to_html()" not in command:
		result=result.replace('\n', '<br/>')
		result=result.replace(' ', '&nbsp;')
	#print(result)
	return result
