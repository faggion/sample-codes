class TestWorker < ApplicationController
  include Sidekiq::Worker
  include Sidetiq::Schedulable
  sidekiq_options queue: :test, retry: 5

  recurrence { minutely(1) }
  
  def perform()
    #Rails.logger.info(title)
    #p 'work: title=' + title
    p DateTime.now.to_s
  end
end
