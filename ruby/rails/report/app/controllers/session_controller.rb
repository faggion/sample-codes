# -*- coding: utf-8 -*-
class SessionController < ApplicationController
  def create
    session["user_info"] = request.env["omniauth.auth"].try(:[], "info")
    redirect_to tool_admin_top_path
  end

  def destroy
    session["user_info"] = nil
    redirect_to :root
  end
end
