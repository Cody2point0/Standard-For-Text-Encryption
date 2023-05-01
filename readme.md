Encrypt:

STEP 1:

call doubledPaddedSignedBytelist(operation, data, pad, operation For Read Statments)

#################################################################################
operation:

'sign':

to make an encryption-ready string needing to be bytes

'read':

  operation For Read Statments
  
  'ASCII':
  
  to return ASCII ord() list from an encryption-ready string needing to be bytes
  
  'string':
  
  to return string containing the data that the encryption-ready string needing to be bytes contains
#################################################################################

STEP 2:

call strToEncryptableBytes(encryption-ready string needing to be bytes)

#################################################################################
Returns the encryption-ready string needing to be bytes formatted as an encryption-ready Bytestring
#################################################################################

STEP 3:

call gen_key(password)

#################################################################################
returns a base64 URL-Safe 32-bit bytestring based off password input. password must be a string
#################################################################################

STEP 4:

call Encrypt(encryption-ready Bytestring, base64 URL-Safe 32-bit Bytestring based off password)

#################################################################################
returns encryption-ready Bytestring encrypted with base64 URL-Safe 32-bit Bytestring Based Off Password
#################################################################################

Decrypt: