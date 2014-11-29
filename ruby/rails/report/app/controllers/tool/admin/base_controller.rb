# -*- coding: utf-8 -*-
class Tool::Admin::BaseController < ApplicationController
  protect_from_forgery with: :exception
  add_flash_types :error

  protected

  def current_user
    @current_user ||= session[:user_info] if session[:user_info]
  end

  helper_method :current_user

  def authenticate
    redirect_to '/tool/admin/login' unless current_user
  end
end
