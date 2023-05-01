def callError(error):
  print(errors[error])
  if round(error) == 0:
    raise ValueError()


errors = {
  00.0001: 'Value Cannot Be Empty',
  01.0002: 'Pad Error, See Errors.txt',
  00.0003: 'Value "operation" Must Be "sign" or "read"'
}
