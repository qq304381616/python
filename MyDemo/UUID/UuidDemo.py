

import uuid

def getUuid():
	return str(uuid.uuid1()).replace("-", "")

if __name__ == '__main__':
    print(getUuid())