
log_file = "log.txt"

def append_log(entry):
    with open(log_file, "a+") as log:
        log.write(entry+"\n")

def read_log():
    entries = []
    with open(log_file) as log:
        for line in log.readlines():
            entries.append(line.rstrip("\n"))
    return entries

def clear_log():
    purge = False
    with open(log_file) as log_read:
        lines = log_read.readlines()
        if len(lines) >= 25:
            lines = lines[20:]
            purge = True

    if purge:
        with open(log_file, "w") as log_write:
            for line in lines:
                log_write.writelines(line)
