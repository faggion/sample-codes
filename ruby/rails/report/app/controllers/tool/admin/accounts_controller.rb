# -*- coding: utf-8 -*-
class Tool::Admin::AccountsController < Tool::Admin::BaseController
  before_filter :authenticate
  
  def index
    @accounts = ::Account.all()
  end

  def show
  end

  def update
    redirect_to tool_admin_accounts_path, :notice => "更新しました"
  end

  def create
    account = ::Account.create(status: params[:status].to_i,
                               name: params[:name])
    account.save
    redirect_to tool_admin_accounts_path, :notice => "作成しました"
  end

  def destroy
    redirect_to tool_admin_accounts_path, :notice => "削除しました"
  end
end
