class Users::ConfirmationsController < Devise::ConfirmationsController
  before_action :authenticate_user!

  private

  #def after_confirmation_path_for(resource_name, resource)
  #  Rails.logger.info("******* after_confirmation_path_for")
  #  sign_out(resource) if signed_in?(resource_name)
  #  new_session_path(resource_name)
  #end
end
