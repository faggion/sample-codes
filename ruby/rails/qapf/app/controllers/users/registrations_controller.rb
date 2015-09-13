# coding: utf-8
class Users::RegistrationsController < Devise::RegistrationsController
  protected

  ## NOTE: signup完了した後に呼び出される
  def after_sign_up_path_for(resource)
    Rails.logger.info("******* after_sign_up_path_for")
    destroy_user_session_path
  end
  
  def after_inactive_sign_up_path_for(resourse)
    Rails.logger.info("******* after_inactive_sign_up_path_for")
    new_user_session_path
  end

  ## NOTE: パスワードやメールアドレスが変更になった場合に呼び出される
  #def after_update_path_for(resource)
  #  Rails.logger.info("*** after_update_path_for ***")
  #end
end
