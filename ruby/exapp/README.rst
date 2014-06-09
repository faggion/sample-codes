
::
  
  midir exapp && cd exapp
  echo 'source "https://rubygems.org"' > Gemfile
  echo 'gem "rails"' >> Gemfile
  bundle install --path vendor/bundle
  bundle exec rails new .
