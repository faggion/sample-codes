<?php

require('Client.php');
require('GrantType/IGrantType.php');
require('GrantType/AuthorizationCode.php');

const CLIENT_ID     = '114786097777.apps.googleusercontent.com';
const CLIENT_SECRET = 'HeLYCnHl5R9vPy-AxW2NxUSm';

const REDIRECT_URI           = 'http://localhost/~satoshi.tanaka/oauth2/callback';
const AUTHORIZATION_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth';
const TOKEN_ENDPOINT         = 'https://accounts.google.com/o/oauth2/token';
const SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email';

$client = new OAuth2\Client(CLIENT_ID, CLIENT_SECRET);

if (!isset($argv[1])) {
    $auth_url = $client->getAuthenticationUrl(AUTHORIZATION_ENDPOINT,
                                              REDIRECT_URI,
                                              array('scope'=>SCOPE));
    error_log($auth_url);
    //header('Location: ' . $auth_url);
    die('Redirect');
}
else {
    error_log($argv[1]);
    $params = array('code' => $argv[1], 'redirect_uri' => REDIRECT_URI);
    $response = $client->getAccessToken(TOKEN_ENDPOINT, 'authorization_code', $params);
    var_dump($response);
    //parse_str($response['result'], $info);
    $info = $response['result'];
    //var_dump($info);
    $client->setAccessToken($info['access_token']);
    $response = $client->fetch('https://www.googleapis.com/oauth2/v1/userinfo');
    var_dump($response, $response['result']);
}
