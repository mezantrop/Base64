# A very simple Base64 encoder/decoder in Python for learning purposes

Almost the same, but in [C](https://github.com/mezantrop/ts-warp/blob/master/base64.c)

## Usage

```Python3

import Base64

print(Base64.Base64().encode('Many hands make light work.'))
TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu
print(Base64.Base64().decode('TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu'))
'Many hands make light work.'
```
