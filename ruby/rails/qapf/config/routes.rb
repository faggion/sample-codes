require 'sidekiq/web'
require 'sidetiq/web'

Rails.application.routes.draw do
  namespace :my do
    get '/' => 'base#index'
  end

  devise_for :users, controllers: { confirmations: 'users/confirmations',
                                    registrations: 'users/registrations' }
  get '/' => 'service#index'
  get '/home' => 'home#show'

  mount Sidekiq::Web, at: "/sidekiq"
end
