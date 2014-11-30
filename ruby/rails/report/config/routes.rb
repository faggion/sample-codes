# coding: utf-8
Rails.application.routes.draw do
  get "/auth/google_oauth2/callback" => "session#create"
  post "/logout" => "session#destroy", :as => :logout
  
  namespace :tool do
    namespace :admin do
      get '/' => 'reports#summary', :as => :top
      # FIXME: login画面
      get "/login" => redirect("/auth/google_oauth2"), :as => :login

      resources :users
      resources :accounts
    end
  end
end
