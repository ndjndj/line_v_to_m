# フロー

|client||server|
|-|-|-|
|movie 送信|→|s3 保管|
|||token 生成|
|受信|←|message, token 送信|
|picture 送信|→|movie 生成|
|||署名付き URL 発行|
|受信|←|署名付き URL, message 送信|
