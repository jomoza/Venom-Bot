import datetime

class logInfo(object):
    """docstring for logInfo."""
    def __init__(self):
        self.file = open('log/log.txt','a')
        pass

    def writeLog(self, tolog):
        now = datetime.datetime.now()
        log = f"\n{str(now)} \n {tolog}"
        self.file.write(log)
        self.file.close()
