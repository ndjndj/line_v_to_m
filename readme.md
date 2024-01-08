# フロー

|client||server|
|-|-|-|
|message 送信|→|token 生成|
|受信|←|message 送信|
|movie 送信|→|s3 保管|
|受信|←|message 送信|
|picture 送信|→|movie 生成|
|||署名付き URL 発行|
|受信|←|署名付き URL, message 送信|

# table 

|pk|sk|item|example|description|
|-|-|-|-|-|
|line id|status||received-movie||
|line id|active-token||202412021233321-faekv23mfgseg||
|line id|picture-path||line-id/picture/||
|line id|movie-path||line-id/movie/||
