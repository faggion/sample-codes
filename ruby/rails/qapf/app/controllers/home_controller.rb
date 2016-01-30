# coding: utf-8
class HomeController < ActionController::Base
  def show
    #Rails.logger.info(DateTime.now.to_s)
    #TestWorker.perform_in(1.minutes, DateTime.now.to_s)
    #render :text => 'added to sidekiq queue'
    render :text => 'do nothing'
  end
end
