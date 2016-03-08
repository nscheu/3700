def add_to_log(msg):
    log = open("log.txt", "a")
    log.write(msg + "\n")
    log.close()