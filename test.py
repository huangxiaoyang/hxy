#!/usr/bin/env python
import paramiko

hostname='10.0.250.102'
username='ops'
pk_path='/Users/hxy/.ssh/hadoop_id_rsa'

ssh=paramiko.SSHClient() 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.load_system_host_keys('/Users/hxy/.ssh/known_hosts') 
ssh.connect(hostname,2208,username,pk_path) 
stdin,stdout,sterr=s.exec_command("date") 
print stdout.read().strip() 
ssh.close()
