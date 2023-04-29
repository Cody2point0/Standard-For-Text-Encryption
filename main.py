import error
import base64
import hashlib
import settings as conf

dataList = []
'''
#################################################
WHEN DONE WITH CODE SESSION ALERT CODY2POINT0 TO COMMIT TO DEVELOPMENT BRANCH GIT
#################################################
'''
log = []
def checkPad(pad:bytes, data:bytes, front:bool=True):
  '''
  returns a boolean identifier that states if data-pad is equal to pad
  '''
  frontValue = None
  if pad == b'':
    error.callError(01.0002)
    return None
  if pad == data[:len(pad)]:
    frontValue = True
  elif pad != data[:len(pad)]:
    frontValue = False
  return frontValue


def doubleList(list):
  '''
  returns a list in witch every value is duplicted in the index following the orign value
  '''
  temp = []
  for i in range(len(list)):
    for j in range(2):
      temp.append(list[i])
  return temp


def padBytes(data:bytes, pad:bytes):
  '''
  Pads a byte string with another byte string at the begenning, end, or both depending on paramaters
  '''
  try:
    temp = [pad]
    temp.append(data)
    return b''.join(temp)
  except TypeError:
    error.callError(01.0002)
    return None


def doubledPaddedSignedBytestring(operation:str, data:bytes, pad:bytes=b' ', returnForRead:str='ASCII'):
  '''
  Due to tri-digit ASCII values, messages and pads are limited to capital letters only.

  when operation = 'sign':
  takes input of data and a padding for the data (default ' '), and combines them, doubles every byte immedeatly following the parent byte, than returns it as an string

  when operation = 'read':
  takes input of already padded data in string of numbers then returns it as either a list of ASCII values or a string containing the data contained in the string of ASCII char identifiers
  '''
  if operation == 'sign':
    signedByteString = padBytes(data, pad)
    signedDoubledASCIIByteList = doubleList(list(signedByteString))
    signedDoubledASCIIByteList = [str(i) for i in signedDoubledASCIIByteList]
    return ''.join(signedDoubledASCIIByteList)
  elif operation == 'read':
    signedDoubledASCIIBytestring = data
    signedDoubledASCIIBytelist = list(signedDoubledASCIIBytestring)
    temp = []
    log.append('START FOR LOOP - CREATION OF TEMP')
    for i in range(0, len(signedDoubledASCIIBytelist), 2):
      temp.append(''.join([signedDoubledASCIIBytelist[i], signedDoubledASCIIBytelist[i + 1]]))
      log.append('')
      log.append('----------')
      log.append('i')
      log.append(str(i))
      log.append('temp')
      log.append(str(temp))
    log.append('END FOR LOOP - END OF TEMP')
    log.append('START DEBUG OF INDIVIDUAL STATMENTS')
    log.append('signedDoubledASCIIBytestring')
    log.append(str(signedDoubledASCIIBytestring))
    log.append('signedDoubledASCIIBytelist')
    log.append(str(signedDoubledASCIIBytelist))
    log.append('temp')
    log.append(str(temp))
    n = 2
    del temp[n - 1::n]
    log.append('new temp')
    log.append(str(temp))
    if returnForRead == 'ASCII':
      return temp
    elif returnForRead == 'string':
      temp2 = []
      log.append('BEGIN FOR LOOP - CREATION OF STRING FROM TEMP USING TEMP2')
      log.append('--------------------')
      for i in range(len(temp)):
        temp2.append(chr(int(temp[i])))
        log.append('i')
        log.append(str(i))
        log.append('temp[i]')
        log.append(str(temp[i]))
        log.append('temp2[i]')
        log.append(str(temp2[i]))
        log.append('--------------------')
      log.append(''.join(temp2))
      log.append('END TEMP AND TEMP2 CREATION TO STRING')
      return ''.join(temp2)
  else:
    error.callError(00.0003)
    return None

def strToEncryptableBytes(string:str):
  return string.encode('UTF-8')

def gen_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))



def getData(data, pad):
  dataList.append(str(data).encode('UTF-8'))
  dataList.append(str(pad).encode('UTF-8'))
getData('DATA', 'PAD')

padded = padBytes(dataList[0], dataList[1])

#lOG APPLY CUSTOM TESTS
log.append('BEGIN CUSTOM TESTS')
log.append('dataList[0]')
log.append(str(dataList[0]))
log.append('dataList[1]')
log.append(str(dataList[1]))
log.append('list(padded)')
log.append(str(list(padded)))
log.append('padded')
log.append(str(padded))
log.append('len dataList[1]')
log.append(str(len(dataList[1])))
log.append('len dataList[0]')
log.append(str(len(dataList[0])))
log.append('checkpad dataList[1] + padded (data)')
log.append(str(checkPad(dataList[1], padded)))
log.append('ASCII value string')
log.append(str(doubledPaddedSignedBytestring('sign', dataList[0], dataList[1])))
log.append('doubleFunc')
log.append(str(doubledPaddedSignedBytestring('read', doubledPaddedSignedBytestring('sign', dataList[0], dataList[1]), dataList[1], 'string')))
log.append('END CUSTOM TESTS')
log.append('\n\n\n')
log.append('RAW LOG LISTFILE')
log.append('\n')
log.append(str(log))
#LOG END APPLY CUSTOM TESTS
if conf.dev == True:
  with open('log.txt', 'w') as logFile:
    for i in range(len(log)):
      logFile.write(log[i])
      logFile.write('\n')