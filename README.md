# A very simple Base64 encoder/decoder in Python for learning purposes

<a href="https://www.buymeacoffee.com/mezantrop" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

Almost the same, but in [C](https://github.com/mezantrop/ts-warp/blob/master/base64.c)

## Usage

```Python3

import Base64

print(Base64.Base64().encode('Many hands make light work.'))
TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu
print(Base64.Base64().decode('TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu'))
'Many hands make light work.'
```
