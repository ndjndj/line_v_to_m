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
|U_#line id|information||||
|U_#line id|current-status||received-movie||
|U_#line id|current-signatured-url||||
|U_#line id|current-token||{yyyymmddhhmmss}-{uuid}||
|U_#line id|current-picture-path||line-id/picture/active-token||
|U_#line id|current-movie-path||line-id/movie/active-token||
|U_#line id|past-{token}|token, status|||
