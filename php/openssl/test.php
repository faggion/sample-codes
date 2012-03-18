<?php
/**
 * $ openssl genrsa -out privkey_rsa.pem
 * $ openssl rsa -pubout -in privkey_rsa.pem -out pubkey_rsa.pem
 *
 * @see http://blog.local.ch/archive/2007/10/29/openssl-php-to-java.html
 */
// 公開鍵・秘密鍵を保存したディレクトリ
define('CERT_DIR', '.');

// 暗号化するデータ
$data = "小池さんはラーメン大好き";
echo "data : " . $data . "\n";

// 公開鍵を読み込む
$public_key = openssl_pkey_get_public(file_get_contents(CERT_DIR . "/pubkey_rsa.pem"));

// 暗号化処理
openssl_seal($data, $encrypted_data, $env_key, array($public_key));
echo "encrypted data : " . base64_encode($encrypted_data) ."\n";
echo "env_key : " . base64_encode($env_key[0]) ."\n";

// 鍵リソースの解放
openssl_free_key($public_key);


// 秘密鍵を読み込む
$private_key = openssl_pkey_get_private(file_get_contents(CERT_DIR . "/privkey_rsa.pem"));

// 復号処理
if (!openssl_open($encrypted_data, $decrypted_data, $env_key[0], $private_key)) {
    die(openssl_error_string() . "\n");
}
// 鍵リソースの解放
openssl_free_key($private_key);

echo "decrypted data : " . $decrypted_data . "\n";

echo 'validate : ' . ($data == $decrypted_data ? 'true' : 'false') . "\n";