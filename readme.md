# フロー

|client||server|
|-|-|-|
|movie 送信|→|s3 保管|
|受信|←|message 送信|
|picture 送信|→|movie 生成|
|||署名付き URL 発行|
|受信|←|署名付き URL, message 送信|

# table 

|pk|sk|description|
|-|-|-|
|line id|current|{mode:"movie", movie-path: "", picture-path: [""],}|
|line id|information||
