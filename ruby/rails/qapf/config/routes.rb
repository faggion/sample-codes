Rails.application.routes.draw do
  namespace :my do
    get '/' => 'base#index'
  end

  devise_for :users, controllers: { confirmations: 'users/confirmations',
                                    registrations: 'users/registrations' }
  get '/' => 'service#index'
end
