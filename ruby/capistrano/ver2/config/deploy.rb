# sudo dscl . append /Groups/wheel GroupMembership satoshi
set :user, "satoshi"

set :application, "tanarky_test"
set :repository,  "https://github.com/tanarky/sample-codes.git"
set :scm, :git

role :app, "localhost"

set :deploy_to, "/tmp/deploy/#{application}"

