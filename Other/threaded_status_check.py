import paramiko
import time
from concurrent.futures import ThreadPoolExecutor


"""Checks that all hosts in the list cycle through the provided states (e.g. a restart) after a relevant command was issued"""

def return_node_status(host, user="username", pw="password"):
    cmd = "api:status"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=pw)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        #output may have to be formatted like here
        #turn bytes to string, split at "":""; remove attached "\n" and strip leading whitespace
        output = str(ssh_stdout.read()).split(":")[1][:-3].strip()
        return(fr"{output}")
    except Exception as e:
        print(e)
        raise e
    finally:
        ssh.close()

def cycle_status(node):
    node_status = return_node_status(node)
    status_list = ["STATE_ONE", "STATE_TWO", "STATE_THREE"]
    for status in status_list:
        timeout = 60
        while timeout > 0:
            if node_status not in status:
                print(f"{node} has status {node_status} and not {status}")
                node_status = return_node_status(node)
                timeout -= 1
                time.sleep(1)
            else:
                print(f"Success! {node} has status {node_status}")
                break
        if timeout <= 0:
            raise AssertionError(f"{node} does not have status {status}. Actual status is {node_status}")
    return f"{node} has cycled successfully"


def threaded_check(nodes):
    with ThreadPoolExecutor() as executor:
        furture = executor.map(cycle_status, nodes)
        #future = promise
        return_value = [i for i in future]
        print(return_value)
    return return_value


#threaded_check(['node1.ipaddress.net', 'node2.ipaddress.net', ...])