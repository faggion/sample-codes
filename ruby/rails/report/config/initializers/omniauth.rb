require 'omniauth-google-oauth2'

HOSTED_DOMAIN = 'glossom.co.jp'

if Rails.env.development?
  Rails.application.config.middleware.use OmniAuth::Builder do
    provider :google_oauth2,
             '1067478220185-ug58t6bnv8oac1febj1flmd72j3p71li.apps.googleusercontent.com',
             'NQJqVq0RbHex_BEDwKngmyvp', {
               hd: HOSTED_DOMAIN
             }
  end
end
