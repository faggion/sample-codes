<?php
// 暗号化するデータ
//$data = '小池さんはラーメン大好き';
$data = '12345678';
$base64_data = base64_encode($data);
echo "data : " . $data . "\n";

// 暗号化キー
$key = 'abcdefgh';

/**
 * 初期化ベクトルを用意する
 * Windowsの場合、MCRYPT_DEV_URANDOMの代わりにMCRYPT_RANDを使用する
 */
$iv = mcrypt_create_iv(mcrypt_get_iv_size(MCRYPT_BLOWFISH, 
                                          MCRYPT_MODE_ECB),
                       MCRYPT_DEV_URANDOM);

// 事前処理
$resource = mcrypt_module_open(MCRYPT_BLOWFISH, '',  MCRYPT_MODE_ECB, '');

// 暗号化処理
mcrypt_generic_init($resource, $key, $iv);
$encrypted_data = mcrypt_generic($resource, $base64_data);
mcrypt_generic_deinit($resource);

echo "encrypted data : " . base64_encode($encrypted_data)."\n";


// 復号処理
mcrypt_generic_init($resource, $key, $iv);
$base64_decrypted_data = mdecrypt_generic($resource, $encrypted_data);
mcrypt_generic_deinit($resource);

$decrypted_data = base64_decode($base64_decrypted_data);
echo "decrypted data : " . $decrypted_data . "\n";

echo 'validate : ' . ($data == $decrypted_data ? 'true' : 'false') . "\n";

// モジュールを閉じる
mcrypt_module_close($resource);