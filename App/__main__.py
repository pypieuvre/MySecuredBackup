import sys

import logbook
import MySecuredBackup as app
import MySecuredBackupConfig as config

log = logbook.Logger(__name__)


def main():
    logbook.StreamHandler(sys.stdout, level='WARNING').push_application()
    logbook.FileHandler('esync.log', level='DEBUG').push_application()
    log.debug('loaded config: {}', config)

    a = app.MySecuredBackupInstance(config)
    for path in a.scan():
        print(path)
		#a.add(path)
    #a.commit()


if __name__ == '__main__':
    main()
