# asyncio.run(gptbz.test())

import requests

image = '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'

response = requests.get('https://ocr.holey.cc/ncku?base64_str=%s' % image)  # .split('base64,')[1])
print(response.content)
